import datetime, time

def countdown(date):
    seconds = convert_to_seconds(date)
    while seconds > 0:
        print(f"Time till deadline for your goal: {goal} is: {int(seconds)} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Countdown complete!")

def convert_to_seconds(future_date):
    now = datetime.datetime.now()
    day, month, year = map(int, future_date.split('.'))
    future = datetime.datetime(year, month, day)
    time_difference = (future - now).total_seconds()
    return time_difference

#user_input = input("Enter your goal:deadline(dd.mm.yyyy)\n> ")
user_input = "test_goal:28.07.2023"
input_list = user_input.split(":")
goal = input_list[0]
deadline_date = input_list[1]

countdown(deadline_date)