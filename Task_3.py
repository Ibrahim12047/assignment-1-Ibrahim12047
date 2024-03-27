# Your solution comes here
output = "a"
day = int(input(" day "))
month = int(input(" month "))
year = int(input(" year "))


leapyear = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

if month == 2:
    if leapyear and day == 29:
        day = 1
        month = 3
    elif not leapyear and day == 28:
        day = 1
        month = 3
    elif day < 28 or (leapyear and day < 29):
        day =day+ 1
    else:
        output = "error"

elif month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10:
    if day == 31:
        day = 1
        month =month+1
    elif day < 31:
        day =day+ 1
    else:
        output = "error"
elif month == 12:
    if day == 31:
        day = 1
        month = 1
        year= year+1
    elif day < 31:
        day =day+ 1
    else:
        output = "error"
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1
    elif day < 30:
        day=day+ 1
    else:
        output = "error"

else:
    output = "error"

if output == "a":
    output = f"{day}.{month}.{year}"
print(output)
