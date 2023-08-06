# 18 Python Projects for your Resume
# №7: Calendar Reminder

from datetime import datetime, timedelta

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

class Reminder:
    def __init__(self, name, date):
        self.name = name
        self.date = date
    
    def get_reminder_info(self):
        print(f"{GREEN}{self.name}{RESET}:{GREEN}{self.date}{RESET}")

today = datetime.now()

reminders = [
    Reminder("Learn Python", today.strftime("%d:%m:%Y")),
    Reminder("Doctor's Appointment", (today + timedelta(days=7)).strftime("%d:%m:%Y")),
    Reminder("Dinner with Friends", (today + timedelta(days=14)).strftime("%d:%m:%Y")),
    Reminder("Birthday Party", (today + timedelta(days=21)).strftime("%d:%m:%Y")),
    Reminder("Work Presentation", (today + timedelta(days=30)).strftime("%d:%m:%Y")),
    Reminder("Annual Check-up", (today + timedelta(days=365)).strftime("%d:%m:%Y"))
]

def show_menu():
    print("Calendar Reminder")
    print("1. Create Reminder")
    print("2. View Reminders")
    print("3. Check Today's Reminders")

def create_reminder():
    while True:
        rem_name = input("Enter reminder name: ")
        if rem_name.lower() in ('q',''):
            break
        while True:
            rem_date = input("Enter reminder date (dd:mm:yyyy) or 'today': ")
            if rem_date.lower() == 'q':
                return
            elif rem_date == 'today':
                reminders.append(Reminder(rem_name, today.strftime("%d:%m:%Y")))
                return
            try:
                datetime.strptime(rem_date, "%d:%m:%Y")
                reminders.append(Reminder(rem_name, rem_date))
                return
            except ValueError:
                print_error("Enter date in (dd:mm:yyyy) format")
                continue

def view_reminders():
    for item in reminders:
        item.get_reminder_info()
    print()

def check_today():
    today_str = today.strftime("%d:%m:%Y")
    for item in reminders:
        if item.date == today_str:
            item.get_reminder_info()
    print()

def main():
    menu_options = {
        1: create_reminder,
        2: view_reminders,
        3: check_today
    }
    print(f"Type ({RED}q{RESET}) to quit\n")
    while True:
        show_menu()
        user_input = input(f"Enter your choice (1-{len(menu_options)}): ")
        print()
        if user_input.lower() in ('q', 'quit', 'exit'):
            break 
        try:
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
    print(f"\n{RED}{message}{RESET}\n")

main()