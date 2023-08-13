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

def days_to_units(days, unit=DEFAULT_UNIT):
    if days > 0:
        unit_conversion = TIME_UNITS.get(unit)
        if unit_conversion is not None:
            return f"{days} days are {days * unit_conversion} {unit}"
        return f"'{unit}' is not a valid unit."
    elif days == 0:
        return "No calculation for zero."
    else:
        return "Negative value entered."

def process_days_list(days_list_string):
    days_set = set(days_list_string.split(','))
    return [days_to_units_or_error(day_str.strip()) for day_str in days_set]

def days_to_units_or_error(day_str):
    try:
        day_int = int(day_str)
        return days_to_units(day_int)
    except ValueError:
        return f"'{day_str}' is not a valid integer. Please try again."

def process_days_and_unit(days_string):
    try:
        days, unit = days_string.split(':')
        return {"days": int(days.strip()), "unit": unit.strip()}
    except ValueError:
        return f"Invalid format. Please use 'days:unit'."

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
                outputs = process_days_list(user_input)
                for output in outputs:
                    print(output, end="\n\n")
            elif ':' in user_input:
                output = process_days_and_unit(user_input)
                if isinstance(output, dict):
                    days = output["days"]
                    unit = output["unit"]
                    print(days_to_units(days, unit), end="\n\n")
                else:
                    print(output, end="\n\n")
            else:
                print(days_to_units_or_error(user_input), end="\n\n")
        except EOFError:  # catch Ctrl+D command and exit
            break
        except KeyboardInterrupt:  # catch Ctrl+C command and exit
            break

if __name__ == "__main__":
    main()
