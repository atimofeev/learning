"""To-Do List Manager.

№2: 18 Python Projects for your Resume
"""
tasks = [
    "Buy groceries",
    "Walk the dog",
    "Finish the report",
    "Call the dentist"
]

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def show_menu():
    """Display menu options."""
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")


def add_task():
    """Add new task to task list."""
    new_task = input("Enter task name: ")
    if new_task != "":
        tasks.append(new_task)
    print()


def show_tasks():
    """Show current tasks list."""
    if not tasks:
        print_error("There are no tasks available")
        return
    i = 0
    print()
    for item in tasks:
        i += 1
        print(f"{i}. {GREEN}{item}{RESET}")
    print()


def select_task(task_action):
    """Task selection for mark/delete action."""
    while True:
        if not tasks:
            print_error(f"There are no tasks to {task_action}")
            break
        print(f"Select task to {task_action}:")
        show_tasks()
        try:
            user_input = input("> ")
            if user_input.lower() in ('q', 'quit', 'exit', ''):
                print()
                break
            user_input = int(user_input) - 1
            if user_input < len(tasks):
                return user_input
            else:
                print_error(f"Provide correct task number (1-{len(tasks)})")
                continue
        except ValueError:
            continue


def mark_completed():
    """Mark task completed."""
    task = select_task("mark")
    if task is not None:
        if tasks[task].endswith("✅"):
            print_error("Task is already marked")
            return
        tasks[task] = f"{tasks[task]} ✅"
        print(f"{GREEN}{tasks[task]}{RESET}\n")
    return


def delete_task():
    """Delete selected task."""
    task = select_task("delete")
    if task is not None:
        temp_task_var = tasks[task]
        tasks.pop(task)
        print(f"\nTask {GREEN}{temp_task_var}{RESET} was removed\n")
    return


def main():
    """Interactively handle user input."""
    menu_options = {
        1: add_task,
        2: show_tasks,
        3: mark_completed,
        4: delete_task
    }
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        show_menu()
        try:
            user_input = input("Enter your choice (1-4): ")
            print()
            if user_input.lower() in ('q', 'quit', 'exit'):
                break
            user_input = int(user_input)
            menu_options[user_input]()
        except KeyError:
            continue
        except ValueError:
            continue
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break


def print_error(message):
    """Print colored error."""
    print(f"\n{RED}{message}{RESET}\n")


main()
