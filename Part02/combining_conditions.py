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

