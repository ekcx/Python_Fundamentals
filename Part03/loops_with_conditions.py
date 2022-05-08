number = 2

while number <= 30:
    print(number)
    number += 2

print("Are you ready?")
number = int(input("Please type in a number: "))

while number > 0:
    print(number)
    number -= 1

print("Now!")


new_value = 1
check_value = int(input("Type the limit: "))
n = int(input("The base: "))

while new_value < check_value:
    print(new_value)
    new_value = new_value*n
