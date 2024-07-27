from colorama import Fore, Style, init
from dotenv import load_dotenv
from src.agent import Agent
from src.prompts import SALES_CHATBOT_PROMPT
from src.tools_schema import tools
from src.utils import clean_output, add_initial_message
from src.tools import (
    FileSearchTool,
    get_product_recommendation,
    generate_calendly_invitation_link,
    generate_stripe_payment_link
)

# Load environment variables from a .env file
load_dotenv()

# Choose any model with LiteLLM
model = "groq/llama3-70b-8192"
# model = "groq/llama-3.1-70b-versatile"
# model = "gemini/gemini-1.5-flash"

# Initiate the File RAG search tool
file_search = FileSearchTool()

# Set the dict of available tool for the agent
available_functions = {
    "get_store_info": file_search.get_store_info,
    "get_product_recommendation": get_product_recommendation,
    "generate_calendly_invitation_link": generate_calendly_invitation_link,
    "generate_stripe_payment_link": generate_stripe_payment_link
}

# Initiate the sale agent
agent = Agent(
        "Sale Agent", 
        model, 
        tools, 
        available_functions, 
        system_prompt=SALES_CHATBOT_PROMPT
    )

# Add initial/introduction chatbot message
add_initial_message(agent)

print(Fore.BLUE + "Enter discussion with TechNerds Sales Agent! Type 'exit' to end the conversation.")
print(Fore.BLUE + f"Sales Bot: {agent.messages[-1]['content']}")
while True:
    user_input = input(Fore.YELLOW + "You: ")
    if user_input.lower() == 'exit':
        print(Fore.BLUE + "Sales Bot: Goodbye!")
        break
    response = agent.invoke(user_input)
    print(Fore.BLUE + f"Sales Bot: {response}")

