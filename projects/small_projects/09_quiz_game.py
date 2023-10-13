"""Quiz Game.

№9: 18 Python Projects for your Resume
"""
import random
import copy

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


class QuizItem:
    """Simple quiz items implementation."""

    def __init__(self, question, answer):
        """Quiz item init."""
        self.question = question
        self.answer = answer


quiz_items = [
    QuizItem("What is the capital of France?", "Paris"),
    QuizItem("Which gas makes up most of the Earth's atmosphere?", "Nitrogen"),
    QuizItem("What is the chemical symbol for Hydrogen?", "H"),
    QuizItem("What color do you get when you mix yellow and blue?", "Green"),
    QuizItem("Which planet is known as the Red Planet?", "Mars"),
    QuizItem("What is the largest ocean on Earth?", "Pacific"),
    QuizItem("Who wrote 'To Kill a Mockingbird'?", "Lee"),
    QuizItem("What is the currency of Japan?", "Yen"),
    QuizItem("Which language is spoken in Brazil?", "Portuguese"),
    QuizItem("What is the square root of 81?", "9"),
    QuizItem("What is the freezing point of water in Celsius?", "0"),
    QuizItem("Who painted the Mona Lisa?", "DaVinci"),
    QuizItem("Who is known as the 'Father of Computers'?", "Babbage"),
    QuizItem("What is the tallest mountain in the world?", "Everest"),
    QuizItem("What is the hardest natural substance on Earth?", "Diamond"),
    QuizItem("Who discovered gravity?", "Newton"),
    QuizItem("Which element has the atomic number 1?", "Hydrogen"),
    QuizItem("Who wrote '1984'?", "Orwell"),
    QuizItem("What is the smallest planet in our solar system?", "Mercury"),
    QuizItem("Which mammal is capable of true flight?", "Bat")
]


def show_menu():
    """Show menu."""
    print("Quiz Game")
    print("1. Start Quiz")
    print("2. Show Questions")


def start_quiz():
    """Handle game logic."""
    correct_counter = 0
    num_of_questions = 5
    rnd_quiz_items = copy.deepcopy(quiz_items)
    random.shuffle(rnd_quiz_items)
    for item in rnd_quiz_items[:num_of_questions]:
        print(f"{GREEN}{item.question}{RESET}\n")
        user_input = input("> ")
        if user_input.lower() == item.answer.lower():
            print(f"\n{GREEN}Correct!{RESET}\n")
            correct_counter += 1
        else:
            print(f"\n{RED}{item.answer}{RESET}\n")
    print(
        f"Quiz completed!\nCorrect answers: "
        f"{correct_counter}/{num_of_questions}"
    )
    print()


def show_questions():
    """Display questions list."""
    for item in quiz_items:
        print(f"{GREEN}{item.question}{RESET}")


def main():
    """Interactively handle user input."""
    menu_options = {
        1: start_quiz,
        2: show_questions
    }
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        show_menu()
        try:
            user_input = input(f"Enter your choice (1-{len(menu_options)}): ")
            print()
            if user_input.lower() in ('q', 'quit', 'exit'):
                break
            user_input = int(user_input)
            if user_input in menu_options:
                menu_options[user_input]()
        except ValueError:
            continue
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break


def print_error(message):
    """Print colored error message."""
    print(f"\n{RED}{message}{RESET}\n")


main()
