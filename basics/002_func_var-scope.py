to_unit = 24
unit = "hours"


def days_to_units(days=20, message=""):
    print(f"{days} days are {days * to_unit} {unit} {message}")


def scope_check():
    local_var = "local_var_test"
    print(f"global var example: {to_unit}")
    print(f"local var example: {local_var}")
    print(f"var from other function: {days, message}") #will throw error


days_to_units()
days_to_units(25)
days_to_units(35, "WOW! 35!")

scope_check()