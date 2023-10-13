# 18 Python Projects for your Resume
# №10 Timer

import time

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def start_timer(duration):
    for _ in range(duration):
        print(f"{GREEN}Time remaining{RESET}: {duration}")
        duration -= 1
        time.sleep(1)
    print()

def main():
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        try:
            user_input = input(f"Start timer [sec]: ")
            print()
            if user_input.lower() in ('q', 'quit', 'exit'):
                break 
            user_input = int(user_input)
            start_timer(user_input)
        except ValueError:
            continue
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break

main()