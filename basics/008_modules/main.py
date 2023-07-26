import my_modules as m
from my_modules import days_to_units, DEFAULT_UNIT, TIME_UNITS


print("Type quit/q/exit for exit")
print("You can use comma (,) delimited lists here")
available_units = ', '.join(TIME_UNITS.keys()) # create a string that is a comma-separated list of the keys of TIME_UNITS
print(f"You can also use colon (:) to specify days:unit[{available_units}]")
print(f"Enter number of days for conversion into {DEFAULT_UNIT}:\n")

while True:
    try:
        user_input = input("> ")
        if user_input in ['quit','exit','q']:  # catch exit keywords
            break
        elif user_input.strip() == "": # remove leading and trailing whitespaces and catch if input was empty
            continue
        elif ',' in user_input:  # catch if a list was entered
            outputs = m.process_days_list(user_input)
            for output in outputs:
                print(output, end="\n\n")
        elif ':' in user_input: # catch dictionary
            output = m.process_days_and_unit(user_input)
            days = output.get("days")
            unit = output.get("unit")
            print(days_to_units(days,unit), end="\n\n")
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