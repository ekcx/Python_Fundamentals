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

# Another example with string comparison

correct = "kittycat"
password = input("Please enter a password: ")

if password == correct:
    print("Correct!")
else:
    print("No Match!")

age = int(input("Please type your age: "))

if age > 18:
    print("You are of age!")
else:
    print("You are not of age!")

goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")


print("Holiday Calendar")
date = input("What is the date today? ")

if date == "Dec 26":
    print("It's Boxing Day")
elif date == "Dec 31":
    print("It's Hogmanay")
elif date == "Jan 1":
    print("It's New Year's Day!")

print("Thanks and Bye.")

number1 = int(input("Please type in the first number:"))
number2 = int(input("Please type in another number:"))

if number1 == number2:
    print("The numbers are equal!")
elif number1 > number2:
    print(f"The greater number was: {number1}")
else:
    print(f"The greater number was: {number2}")



