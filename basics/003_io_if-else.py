to_unit = 24
unit = "hours"


def days_to_units(days):
    if days > 0:
        return f"{days} days are {days * to_unit} {unit}"
    elif days == 0:
        return "No calculation for zero"
    else:
        return "Negative value entered"


user_input = input(f"Enter number of days for conversion into {unit}:\n") # user input

print(days_to_units(int(user_input)))