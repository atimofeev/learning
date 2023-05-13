import openai
from openai import ChatCompletion

# Read api key
with open("key.txt") as f:
    openai.api_key = f.read().strip()

# Create empty list to store message history
history = []

# Send prompt, receive response and save history for both user and assistant
# API does not store any message history on their end
def send(content):
    history.append({"role": "user", "content": content})  # save user prompt to list
    response = ChatCompletion.create(model="gpt-3.5-turbo", messages=history)  # send prompt
    output = response["choices"][0]["message"]["content"]  # parse assistant reply json
    history.append({"role": "assistant", "content": output})  # save assistant reply to list
    return output  # return assistant reply

print("Type quit/q/exit for exit")

while True:  # init forever loop
    try:
        user_input = input ("> ")
        if user_input in ['quit','exit','q']:  # catch exit keywords
            break
    except EOFError:  # catch Ctrl+D command (EOF) and exit
        print("\n")
        break
    except KeyboardInterrupt: # catch Ctrl+C command and exit
        print("\n")
        break
    assistant_output = send(user_input)
    print(assistant_output, end="\n\n")