import instructor
from colorama import Fore, init
from litellm import Router
from .models import models_list

# Initialize colorama for colored terminal output
init(autoreset=True)


class PatchLiteLLM:
    def __init__(self, models_list):
        self.models_list = models_list
        self.client = instructor.patch(Router(model_list=models_list))

    def completion(self, model, messages, **kwargs):
        response = self.client.chat.completions.create(
            model=model, messages=messages, **kwargs
        )
        return response


class Agent:
    """
    @title AI Agent Class
    @notice This class defines an AI agent that can uses function calling to interact with tools and generate responses.
    """

    def __init__(self, name, model, tools=[], system_prompt=""):
        """
        @notice Initializes the Agent class.
        @param model The AI model to be used for generating responses.
        @param tools A list of tools that the agent can use.
        @param available_tools A dictionary of available tools and their corresponding functions.
        @param system_prompt system prompt for agent behaviour.
        """
        self.name = name
        self.model = model
        self.client = PatchLiteLLM(models_list)
        self.messages = []
        self.tools = tools
        if tools:
            self.tools_schemas = self.get_openai_tools_schema()
        self.system_prompt = system_prompt
        if self.system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def invoke(self, message):
        print(Fore.GREEN + f"\nCalling Agent: {self.name}")
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        return result

    def execute(self):
        """
        @notice Executes the AI model to generate a response and handle tool calls if needed.
        @return The final response from the AI.
        """
        # First, call the AI to get a response
        response_message = self.call_llm()

        # Check if there are tool calls in the response
        tool_calls = response_message.tool_calls

        # If there are tool calls, invoke them
        if tool_calls:
            try:
                response_message = self.run_tools(tool_calls)
            except Exception as e:
                print(Fore.RED + f"\nError: {e}\n")
        return response_message.content

    def run_tools(self, tool_calls):
        """
        @notice Runs the necessary tools based on the tool calls from the AI response.
        @param tool_calls The list of tool calls from the AI response.
        @return The final response from the AI after processing tool calls.
        """
        # For each tool the AI wanted to call, call it and add the tool result to the list of messages
        for tool_call in tool_calls:
            self.execute_tool(tool_call)

        # Call the AI again so it can produce a response with the result of calling the tool(s)
        response_message = self.call_llm()
        tool_calls = response_message.tool_calls

        # If the AI decided to invoke a tool again, invoke it
        if tool_calls:
            try:
                response_message = self.run_tools(tool_calls)
            except Exception as e:
                print(Fore.RED + f"\nError: {e}\n")

        return response_message

    def execute_tool(self, tool_call):
        """
        @notice Executes a tool based on the tool call from the AI response.
        @param tool_call The tool call from the AI response.
        @return The final response from the AI after executing the tool.
        """
        function_name = tool_call.function.name
        func = next(
            iter([func for func in self.tools if func.__name__ == function_name])
        )

        if not func:
            return f"Error: Function {function_name} not found. Available functions: {[func.__name__ for func in self.tools]}"

        try:
            print(Fore.GREEN + f"\nCalling Tool: {function_name}")
            print(Fore.GREEN + f"Arguments: {tool_call.function.arguments}\n")
            # init tool
            func = func(**eval(tool_call.function.arguments))
            # get outputs from the tool
            output = func.run()

            self.messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": output,
                }
            )
            return output
        except Exception as e:
            print("Error: ", str(e))
            return "Error: " + str(e)

    def call_llm(self):
        response = self.client.completion(
            model=self.model,
            messages=self.messages,
            **({"tools": self.tools_schemas} if self.tools_schemas else None),
            temperature=0.1,
        )
        response_message = response.choices[0].message

        # Necessary to handle Groq llama3 error
        if response_message.tool_calls is None:
            response_message.tool_calls = []
        if response_message.function_call is None:
            response_message.function_call = {}

        self.messages.append(response_message)

        return response_message

    def get_openai_tools_schema(self):
        return [
            {"type": "function", "function": tool.openai_schema} for tool in self.tools
        ]

    def reset(self):
        self.messages = []
        if self.system_prompt:
            self.messages.append({"role": "system", "content": self.system_prompt})
