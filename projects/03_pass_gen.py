# 18 Python Projects for your Resume
# №3: Password Generator

import random, string

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

MIN_PASS_LEN = 8

def generate_pass(pwd_len):
    types = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    pwd = ""
    for _ in range(pwd_len):
        char = random.choice(random.choice(types))
        new_pwd = pwd + char
        pwd = new_pwd
    print(f"{GREEN}{pwd}{RESET}")

def main():
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        try:
            pass_len = input(f"Enter password length (min {MIN_PASS_LEN}): ")
            if pass_len in ('q', 'quit', 'exit'):
                break
            pass_len = int(pass_len)
            if pass_len < MIN_PASS_LEN:
                continue
            generate_pass(pass_len)
            while True:
                user_input = input("Generate another password? (y/n): ")
                if user_input in ('y', 'yes'):
                    break
                elif user_input in ('n', 'no', 'q'):
                    return
        except ValueError:
            continue
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break

main()