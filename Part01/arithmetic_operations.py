height = 172.5
weight = 68.55
bmi = weight / (height / 100) ** 2
print(f"The BMI is {bmi}")

# Python has a another feature that divides and round down nearest integer by using double slash //

x = 10
y = 4.2
z = x // y # will be display 2
print(z)
z = x / y # will be display floating point number.
print(z)

# Numbers as input
# We are taking the strings with input() method as we know, after taking the string, we can do type casting like this:

your_born = input("When were you born?")
your_age = 2022 - int(your_born)
print("Your age is: ")
print(your_age)

# The best way to learn anything practise.

any_integer = input("Please any integer: ")
print(int(any_integer))

any_integer = input("Please any integer: ")
print(any_integer)

height = float(input("What is your height?"))
weight = float(input("What is your weight?"))
bmi = weight / (height / 100) * 2
print("Your bmi is: ")
print(bmi)

number1 = float(input("Please enter number1"))
number2 = float(input("Please enter number2"))
number3 = float(input("Please enter number3"))
summation = number1 + number2 + number3
print(summation)

