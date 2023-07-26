print("test string")
print(123)
print(228.25)
print(13+37)
#print("20 days are " + 60*24*20 + " minutes") can only concatenate str (not "int") to str
print("20 days are " + str(60*24*20) + " minutes")
print(f"20 days are {60*24*20} minutes") #f = format

days = 25
to_sec = 60*60*24
print(f"{days} days are {days * to_sec} seconds")