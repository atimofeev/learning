# Loosely based on tutorial by TechWorld with Nana
# yt: t8pPdKYpowI

DEFAULT_UNIT = "hours"

TIME_UNITS = {
    "minutes": 1440,
    "hours": 24,
    "days": 1,
    "weeks": 0.14,
    "months": 0.0328767123,
    "years": 0.00273973
}

EXIT_KEYWORDS = ['quit', 'exit', 'q']

def convert_days_to_units(days, unit=DEFAULT_UNIT):
    if days < 0:
        return "Negative value entered."
    if days == 0:
        return "No calculation for zero."
    
    unit_conversion = TIME_UNITS.get(unit)
    if unit_conversion is None:
        return f"'{unit}' is not a valid unit."
    
    return f"{days} days are {days * unit_conversion} {unit}"

def handle_list_input(user_input):
    days_list = user_input.split(',')
    return [convert_single_input(day.strip()) for day in days_list]

def handle_dict_input(user_input):
    try:
        days, unit = user_input.split(':')
        return convert_days_to_units(int(days.strip()), unit.strip())
    except (ValueError, TypeError):
        return "Invalid format. Please use 'days:unit'."

def convert_single_input(day_str):
    try:
        day_int = int(day_str)
        return convert_days_to_units(day_int)
    except ValueError:
        return f"'{day_str}' is not a valid integer. Please try again."

def main():
    print("Type quit/q/exit for exit")
    print("You can use comma (,) delimited lists here")
    print("You can also use colon (:) to specify days:unit[minutes,hours,days,weeks,months,years]")
    print(f"Enter number of days for conversion into {DEFAULT_UNIT}:\n")

    while True:
        try:
            user_input = input("> ").strip()
            if user_input in EXIT_KEYWORDS:
                break
            elif not user_input:
                continue
            elif ',' in user_input:
                outputs = handle_list_input(user_input)
                for output in outputs:
                    print(output, end="\n\n")
            elif ':' in user_input:
                print(handle_dict_input(user_input), end="\n\n")
            else:
                print(convert_single_input(user_input), end="\n\n")
        except EOFError:  # catch Ctrl+D command and exit
            break
        except KeyboardInterrupt:  # catch Ctrl+C command and exit
            break

if __name__ == "__main__":
    main()
