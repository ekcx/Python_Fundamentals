# indentation structure.
# Each indentation depends on tab key.

password = input("What is your name?")

if password == "John":
    print("This is the first print line in if-elif structure")
    print("This is the second print line in if-elif structure")
    print("This is the third print line in if-elif structure")
else:
    print("Password do not match!")

print("\n")
print("This is the end of if-elif structure")

# if-elif needs colon : for every structure.

my_var = int(input("Write an integer: "))

if my_var == 1:
    print("One")
elif my_var == 2:
    print("Two")
elif my_var == 3:
    print("Three")
elif my_var == 4:
    print("Four")
else:
    print("None of them!")


# Boolean Expressions

# This is True
a = 3
condition = a < 5
# Will be display True
print(condition)

# This is False
condition = a > 5
# Will be display False
print(condition)

# It is turning boolean value False to integer 0
condition = int(condition)
print(condition)

# It is turningh boolean value True to integer 1
condition = int(a < 4)
print(condition)

number1 = input("Number1:")
number2 = input("Number2:")
operation = input("Operation")

if operation == "add":
    print(f"{number1} + {number2} = {int(number1) + int(number2)}")
elif operation == "multiply":
    print(f"{number1} * {number2} = {int(number1) * int(number2)}")
elif operation == "subtract":
    print(f"{number1} - {number2} = {int(number1) - int(number2)}")
else:
    print("It is not logical expression!")


