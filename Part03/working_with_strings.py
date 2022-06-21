begin = "ex"
end = "ample"
word = begin+end
print(word)

word = "banana"
print(word*3)

n = 10  # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

get_str = input("Type in a string: ")
get_number = int(input("Type in number: "))
print(get_str * get_number)

input_str = input("Type in a string: ")
print(input_str)
print("+" * len(input_str))

compare_string1 = input("Type a string1: ")
compare_string2 = input("Type a string2: ")

if len(compare_string1) > len(compare_string2):
    print(compare_string1, "is longer than", compare_string2)
elif len(compare_string2) > len(compare_string1):
    print(compare_string2, "is longer than", compare_string1)
else:
    print("Each strings are equal to each other.", compare_string1, "=", compare_string2)

get_str = input("Please enter a string: ")
print(get_str[0])
print(get_str[1])
print(get_str[5])

print("The firs character of the string:", get_str[0])
print("The last character of the string:", get_str[len(get_str)-1])

# There is a negative index in Python.

get_str = input("Type in a string: ")
j = 0

# This will be displaying in reverse order.

for i in range(1, len(get_str)+1):
    j = i * -1
    print(get_str[j])

# -1 is the last index of the string

testing = input("Type in a string: ")
print("First Character: ", testing[0])
print("Last Character: ", testing[-1])

get_str = input("Type a string: ")

if get_str[2] == get_str[-1]:
    print("The second and the last character is the same: ", get_str[2])
else:
    print("The second and the last character is different.")

get_number = int(input("Width:"))
print("#" * get_number)

get_number2 = int(input("Height:"))

for i in range(0, get_number):
    print("#" * get_number2)

get_string = input("Type a string: ")
print(get_string)
print("-"*len(get_string))

get_string = input("Type a string:")
print("*" * (20 - len(get_string)) + get_string)