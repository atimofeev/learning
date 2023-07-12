to_unit = 24
unit = "hours"

def days_to_units(days):
    if days > 0:
        return f"{days} days are {days * to_unit} {unit}"
    elif days == 0:
        return "No calculation for zero."
    else:
        return "Negative value entered."

print("Type quit/q/exit for exit")
print(f"Enter number of days for conversion into {unit}:\n")

while True:  
    try:
        user_input = input("> ")
        if user_input in ['quit','exit','q']:  # catch exit keywords
            break
        user_input = int(user_input)
    except ValueError: # catch if string was entered. retries the loop from start
        print("That's not an integer. Please try again.\n")
        continue
    except EOFError:  # catch Ctrl+D command and exit
        print("\n")
        break
    except KeyboardInterrupt: # catch Ctrl+C command and exit
        print("\n")
        break
    output = days_to_units(user_input)
    print(output, end="\n\n")