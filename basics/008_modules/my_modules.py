DEFAULT_UNIT = "hours"

TIME_UNITS = {
    "seconds": 86400,
    "minutes": 1440,
    "hours": 24,
    "days": 1,
    "weeks": 0.14,
    "months": 0.0328767123,
    "years": 0.00273973
}

def days_to_units(days, unit=DEFAULT_UNIT):
    if days > 0:
        try:
            unit_conversion = TIME_UNITS.get(unit)
            return f"{days} days are {days * unit_conversion} {unit}"
        except TypeError:
            return (f"'{unit}'is not a valid unit.")
    elif days == 0:
        return "No calculation for zero."
    else:
        return "Negative value entered."


def process_days_list(days_list_string):
    days_set = set(days_list_string.split(',')) # split the input string by commas, convert resulting list into a set
    results = []
    for days_set_item in days_set:
        try:
            day_int = int(days_set_item.strip()) # remove leading and trailing whitespaces, try convert to integer
        except ValueError:
            results.append(f"'{days_set_item}' is not a valid integer. Please try again.")
            continue
        results.append(days_to_units(day_int))
    return results


def process_days_and_unit(days_string):
    try:
        days_list = days_string.split(':')
        days_list[0] = int(days_list[0].strip())
        days_list[1] = days_list[1].strip()
        dict = {'days': days_list[0], 'unit': days_list[1]}
    except ValueError:
        return (f"'{days_list[0]}'is not a valid integer. Please try again.")
    return dict