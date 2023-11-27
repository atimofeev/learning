"""Interactive CLI for ChatGPT conversations.

Now with model selection.
"""
import openai
from openai import ChatCompletion
import models_request
import interactive_menu

history = []

with open("openai.key", encoding="utf-8") as f:
    openai.api_key = f.read().strip()


def select_model():
    """Select model via interactive menu."""
    return interactive_menu.select(models_request.get_models())


def send(content, model):
    """Send prompt to ChatGPT, receive assistant reply.

    Append everything to history.
    """
    history.append({"role": "user", "content": content})
    response = ChatCompletion.create(model=model, messages=history)
    output = response["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": output})
    return output


def main():
    """Interactive CLI loop with exceptions handling."""
    try:
        model = select_model()
        print("Type quit/q/exit for exit")
        while True:
            user_input = input("> ")
            if user_input in ['quit', 'exit', 'q']:
                break
            assistant_output = send(user_input, model)
            print(assistant_output, end="\n\n")
    except (EOFError, KeyboardInterrupt):
        print()


main()
