# This script will generate ChatGPT prompt using local files contents
"""Import argsparse for accessing arguments. pyperclip for clipboard access"""
from argparse import ArgumentParser
from pyperclip import copy

PROMPT = """
This is a test promt to check my script functionality.
Please let me know if you are able to parse the info you've been provided with.
"""

def process_file(path):
    """Process files contents"""
    with open(path, 'r') as file:
        content = file.read()
        processed_file = f"\n{path} contents:\n######\n{content}\n######"
    return processed_file

def copy_to_clipboard(data):
    """Copy files contents to clipboard"""
    copy(data)

def main(files):
    """Main function"""
    prompt_and_files = PROMPT
    for file_path in files:
        prompt_and_files += f"\n{process_file(file_path)}"
    copy_to_clipboard(prompt_and_files)

if __name__ == '__main__':
    parser = ArgumentParser(description="Process one or more files.")
    parser.add_argument('files', metavar='file', type=str, nargs='+',
                        help='One or more file paths to process')

    args = parser.parse_args()
    main(args.files)
