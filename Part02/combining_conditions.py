# Logical Operators

number = int(input("Please type in a number: "))
if number >= 5 and number <= 8: # The simplified version is: 5 <= number <= 8
    print("The number is between 5 and 8")
else:
    print("The number is out of limit.")

if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8.")
else:
    print("The number is within the range of 5 to 8.")

# instead of && and ||, python is using AND and OR word.

# Lear Year Calculation

leap_year = int(input("Enter the year: "))

if leap_year % 4 == 0 and leap_year % 100 != 0:
    print(f"{leap_year} is leap year!")
elif leap_year % 400 == 0:
    print(f"{leap_year} is leap year!")
else:
    print(f"{leap_year} is not a leap year!")

# indentation is crucial.

check = int(input("Please enter the number: "))

if check > 0:
    if check % 2 == 0:
        print(f"{check} is a positive and even number.")
    else:
        print(f"{check} is a positive and odd number.")
else:
    print(f"{check} is a negative number.")


