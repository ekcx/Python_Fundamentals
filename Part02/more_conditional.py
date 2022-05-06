number = int(input("Please type in a number: "))

# This is inefficient.
if number < 0:
    print("The number is negative!")
elif number > 0:
    print("The number is positive!")
else:
    print("The number is zero!")

# This can be good!

number = int(input("Please type in a number:"))

if number < 0:
    print("The number is negative!")
else:
    print("The number is positive or zero!")

# It compares the numbers!

number = int(input("Please type in a number: "))

if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")











