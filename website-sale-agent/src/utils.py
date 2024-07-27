
def clean_output(response: str) -> str:
    # Removes the <END_OF_TURN> tag from the given response.
    response = response.replace("<END_OF_TURN>", "").strip()

    return response

def add_initial_message(agent):
    agent.messages.append({"role": "assistant", "content": "Hey, This is Emily from TechNerds. How can I help you?"})


