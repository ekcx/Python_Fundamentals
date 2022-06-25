# The break and continue mechanism
import random

sum = 0

while True:
    number = int(input("Please enter a number, -1 exit: "))

    if number == -1:
        break
    elif number >= 10:
        continue
    else:
        sum += number

print(sum)

# Multiplication

multiplication_number = int(input("Type in a number: "))

for i in range(1, multiplication_number + 1):
    for j in range(1, multiplication_number + 1):
        print(f"{i} x {j} = {i * j}")

print()

factorial = int(input("Type in a factorial number: "))
sum = 1

if factorial == 1:
    print(sum)
elif factorial == 0 or factorial < 0:
    print("Ok bye.")
else:
    for i in range(1, factorial + 1):
        sum *= i
    print(sum)

random_number = int(input("Please type in an integer: "))

for i in range(1, random_number + 1):
    print(random.randint(1, random_number+1))
# Not exactly.