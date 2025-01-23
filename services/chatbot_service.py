import os
from dotenv import load_dotenv
from openai import OpenAI
from services.follow_up import create_follow_up

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = [{"role": "system", "content": "You are a helpful music coach offering practice tips."}]


def reset_conversation():
    """Resets the conversation history to the default system message."""
    global conversation_history
    conversation_history = [{"role": "system", "content": "You are a helpful music coach offering practice tips."}]


def truncate_conversation(max_messages=5):
    """Keeps the conversation history within the specified max_messages limit."""
    global conversation_history
    if len(conversation_history) > max_messages:
        conversation_history = [conversation_history[0]] + conversation_history[-(max_messages - 1):]


def format_tabs(response: str, max_length: int = 40) -> str:
    """
    Formats guitar or bass tabs for small chat bubbles.

    Args:
        response (str): The raw response containing potential tabs.
        max_length (int): The maximum length of a single tab line before splitting.

    Returns:
        str: The formatted response with properly displayed tabs.
    """
    lines = response.split("\n")
    formatted_lines = []
    tab_block = []  # Collect tab lines for multi-line handling

    # Helper function to split long lines
    def split_line(line):
        return line[:max_length].strip() + " \\n " + line[max_length:].strip()

    for line in lines:
        stripped_line = line.strip()
        # Check if the line is a guitar tab line
        if stripped_line and any(stripped_line.startswith(s + "|") for s in "eBGDAE"):
            cleaned_line = stripped_line.replace("| ", "|")  
            tab_block.append(cleaned_line if len(cleaned_line) <= max_length else split_line(cleaned_line))
        else:
            # If a tab block exists, flush it
            if tab_block:
                formatted_lines.extend(tab_block)
                tab_block = []

            formatted_lines.append(stripped_line)

    if tab_block:
        formatted_lines.extend(tab_block)

    return "```\n" + "\n".join(formatted_lines) + "\n```"


def get_openai_response(question: str, reset: bool = False) -> str:
    """
    Handles generating a response using OpenAI's API.
    
    Args:
        question (str): The user's question.
        reset (bool): If True, resets the conversation history.

    Returns:
        str: Response from the chatbot.
    """
    if not question or not question.strip():
        return "Question cannot be empty."
    
    try:
        if reset:
            reset_conversation()

        conversation_history.append({"role": "user", "content": question})
        truncate_conversation(max_messages=5)

        response = client.chat.completions.create(model="gpt-4", messages=conversation_history)
        answer = response.choices[0].message.content.strip()
        
        if "tab" in question.lower() or "tablature" in question.lower():
            answer = format_tabs(answer)

        conversation_history.append({"role": "assistant", "content": answer})

        follow_up_question = create_follow_up(question)
        return f"{answer}\n\n{follow_up_question}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"