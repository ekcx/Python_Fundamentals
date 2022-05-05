# Block
age = 18
if age > 17:
    # beginning of the conditional block.
    print("You are of age!")
    age += 1
    print("You are now one year older...")
    # end of the conditional block.

print("This is the another block.")

# The indentation should be the same for the same blocks.
# Any python programs should be started the leftmost edge. Otherwise, it will not operate.

# To find the data type, we can use type() method.

name = "Anna"
result = 100

print(type(name))
print(type(result))

# Finding the lenght of the string wih "len"

string_length = input("Please enter the string: ")
print("The number of lenght of the string: " + str(len(string_length)))

length_variable = len(string_length)
print(length_variable)

# Empty Strings will display zero.
# The string is empty.

empty = ""
length_variable = len(empty)
print(length_variable)

# Type casting in Python

casting = float(input("Please enter a float number: "))

print(casting)
print(int(casting))

