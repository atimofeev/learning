to_unit = 24
unit = "hours"

def days_to_units(days):
    if days > 0:
        return f"{days} days are {days * to_unit} {unit}"
    elif days == 0:
        return "No calculation for zero."
    else:
        return "Negative value entered."


def split_list(days_list_string):
    days_list = days_list_string.split(',') # Split the input string by commas, which results in a list.
    #days_list = set(days_list_string.split(',')) # convert list to set, which will contain only unique values
    results = []
    for days_list_item in days_list:
        try:
            day = int(days_list_item.strip()) # remove leading and trailing whitespaces, try convert to integer
        except ValueError:
            results.append(f"'{days_list_item}' is not a valid integer. Please try again.")
            continue
        results.append(days_to_units(day))
    return results

print("Type quit/q/exit for exit")
print("You can use comma delimited lists here")
print(f"Enter number of days for conversion into {unit}:\n")

while True:
    try:
        user_input = input("> ")
        if user_input in ['quit','exit','q']:  # catch exit keywords
            break
        elif user_input.strip() == "": # remove leading and trailing whitespaces and catch if input was empty
            continue
        elif ',' in user_input:  # catch if a list was entered
            outputs = split_list(user_input)
            for output in outputs:
                print(output, end="\n\n")
        else: # continue to regular execution with single day
            print(days_to_units(int(user_input)), end="\n\n")

    except ValueError: # catch if string was entered. retries the loop from start
        print("That's not an integer. Please try again.\n")
        continue
    except EOFError:  # catch Ctrl+D command and exit
        print("\n")
        break
    except KeyboardInterrupt: # catch Ctrl+C command and exit
        print("\n")
        break
