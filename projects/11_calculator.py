# 18 Python Projects for your Resume
# №11 Calculator

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else print_error("Division by zero")
}

class Operate:
    def __init__(self, a, b, op):
        self.a = float(a)
        self.b = float(b)
        self.op = op

    def calculate(self):
        result = OPERATIONS.get(self.op, lambda: print_error("Unsupported operation"))(self.a, self.b)
        print(f"{GREEN}{self.a} {self.op} {self.b} = {result}{RESET}")


def select_op(usr_input):
    found_ops = [op for op in OPERATIONS if op in usr_input]
    if len(found_ops) == 1:
        sel_op = found_ops[0]
    elif len(found_ops) > 1:
        print_error("Multiple operations found")
        return
    else:
        print_error("No operation found")
        return
    numbers = usr_input.split(sel_op)
    try:
        a = float(numbers[0])
        b = float(numbers[1])
        Operate(a, b, sel_op).calculate()
    except ValueError:
        print_error("Invalid number format")


def main():
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        try:
            user_input = input(f"Available calc operations: (+ - * /)\nEnter expression: ")
            print()
            if user_input.lower() in ('q', 'quit', 'exit'):
                break
            select_op(user_input)
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break

def print_error(message):
    print(f"\n{RED}{message}{RESET}\n")

main()