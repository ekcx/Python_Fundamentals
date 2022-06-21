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


# The sum of consecutive number

get_limit = int(input("Type a limit: "))
summation = 0
print("The consecutive sum: ")
for i in range(1, get_limit):
    if summation >= get_limit:
        break
    else:
        summation += i
        print(f"{i}")

print(summation)

number = int(input("Please type an integer: "))
limit = 1

while number > limit:
    print(limit)
    limit = limit + 1
    if number < limit:
        break

upper_limit = int(input("Please type upper limit base2: "))
base = 2
summation2 = 1

while summation2 < upper_limit:
    print(summation2)
    summation2 *= base
    if summation2 >= upper_limit:
        break

upper_limit = int(input("Please type upper limit base3:"))
base = 10
summation3 = 1

while summation3 < upper_limit:
    print(summation3)
    summation3 *= base
    if summation3 >= upper_limit:
        break

# Building strings

words = "pride"
words = words + ", prejudice"
words = words + " and Python"

print(words)

# The += operator allows us to write this a little more compactly:

words = "prinde"
words += ", prejudice"
words += " and Python"

print(words)

# This also applies to f-strings..

course = "Introduction to Programming"
grade = 4

verdict = "You have received. "
verdict += f"The grade {grade}"
verdict += f" from the course {course}"

print(verdict)
