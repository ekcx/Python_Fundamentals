#declaring integer type variables

age = 30
star = 5
string_variable = "John Doe"

#strings and integers

my_variable = 30
my_string = "100"

print(my_string + " " + str(my_variable)) #In here, str() method is changing string data type into integer one.

# Printing f-strings
# This is a sexy feature of Python.

# f-string structure depends on the changing string data type to integer with a special f" {string_variable}"
print(f"my_variable is {my_variable}")

# Examples f-string structure

# first declare integer data type.

integer1 = 20
print(f"This is the f-string structure: {integer1}")

integer2 = 10
print(f"This is the f-string structure: {integer2}")

# f-string structure provides using integer data type and string data type together.
# f-string is equivalent with str() method like this:

print("This is the str(): " + str(integer2))
print("This is the type casting by using str(): " + str(integer1))

# f-string's are easiest way to work with different data types in Python.

