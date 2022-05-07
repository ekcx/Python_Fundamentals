words = ["cat", "dog", "pineapple"]

for a in words:
    print(a, len(a))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range() function provides the limits.

for i in range(10):
    print(numbers[i])

even_list = [0, 2, 4, 6, 8]
odd_list = [1, 3, 5, 7, 9]

print("\n")
for i in range(5):
    print(even_list[i])

print("\n")
for i in range(5):
    print(odd_list[i])

while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break
    print(number ** 2)

print("Thanks and bye!")

value = int(input("Please type an integer: "))

while value < 10:
    print(f"{value}")
    value += 1

print("The end of the while.")

while value != 0:
    print(f"The last value is {value}")
    value = int(input("Please type a number again: (0 Exit)"))

print("You entered the 0. Thanks.")

string = ""

while string != "no":
    print("hello!")
    string = input("Shall we continue?")

print("Thanks. Goodbye.")

from math import sqrt

number = 1

while number != 0:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid Number.")
    else:
        print(sqrt(number))

    if number == 0:
        print("Exiting...")

