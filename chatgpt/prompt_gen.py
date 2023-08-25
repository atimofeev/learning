#!/usr/bin/env python3
"""With locally provided files and prompt input,
this code will copy contents to clipboard for web ChatGPT use"""
from argparse import ArgumentParser
from pyperclip import copy

BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
DELIMITER = "######"
PREVIEW_LINES = 10
processed_files = []

def process_files(files):
    """Process files contents"""
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            content = ''.join(f.readlines())
            processed_files.append((f"\n{file} contents:", \
                f"\n{DELIMITER}\n{content}\n{DELIMITER}"))

def preview_files(prompt):
    """Preview selected files"""
    print(f"{gbold('Your prompt:')}\n{prompt}")
    for message, file in processed_files:
        file_preview = '\n'.join(file.split('\n')[1:PREVIEW_LINES+1])
        print(gbold(message))
        print(file_preview)
    if input(f"\n{bold('Do you want to proceed?')} \
        ({gbold('y')}/{rbold('n')}): ").strip().lower() == 'y':
        return
    else:
        exit_program()

def copy_to_clipboard(prompt):
    """Copy files contents to clipboard"""
    data = prompt
    for message, file_content in processed_files:
        data += "\n" + message + file_content
    copy(data)

def main(files):
    """Interactive CLI"""
    print(bold("Files to copy:")+ "\n")
    for file_path in files:
        print(file_path)
    print(f"\n{bold('Enter your prompt')} (type '{rbold('q')}', \
        '{rbold('quit')}', or '{rbold('exit')}' to exit):")
    try:
        user_prompt = input(gbold("> "))
        if user_prompt.lower() in ('q', 'quit', 'exit'):
            exit_program()
        process_files(files)
        preview_files(user_prompt)
        copy_to_clipboard(user_prompt)
        print(gbold("Data copied to clipboard"))
    except (KeyboardInterrupt, EOFError):
        exit_program()

def exit_program():
    """Exit with message"""
    print(rbold("Exit"))
    exit()

def bold(text):
    """Helper func to make text bold"""
    return f"{BOLD}{text}{RESET}"

def gbold(text):
    """Helper func to make text green and bold"""
    return f"{GREEN}{BOLD}{text}{RESET}"

def rbold(text):
    """Helper func to make text red and bold"""
    return f"{RED}{BOLD}{text}{RESET}"

if __name__ == '__main__':
    parser = ArgumentParser(description="Process one or more files.")
    parser.add_argument('files', metavar='file', type=str, nargs='+',
                        help='One or more file paths to process')
    args = parser.parse_args()
    main(args.files)
