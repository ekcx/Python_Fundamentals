my_string = "Exemplary"
print(my_string[2:6])
print()
if my_string[2:6] == "empl":
    print(True)
else:
    print(False)


input_string = "Presumptious"

print(input_string[0:3])
print(input_string[4:10])

# Half-open Intervals
print(input_string[:3])
print(input_string[4:])

# Substring

taking_string = input("Please type a string: ")

for i in range(0, len(taking_string)+1):
    print(taking_string[0:i])

for i in range(0, len(taking_string)+1):
    print(taking_string[-1*len(taking_string)+i])

# Searching in the string
trying_string = "TesT"
print("T" in trying_string)  # It will be displaying True or False
print("O" in trying_string)

input_string = "Special Name"

while True:
    substring = input("What are you looking for? ")
    if substring in input_string:
        print("Found it.")
        break
    else:
        print("Not Found!")

while True:
    input_string = input("Please type in a string: ")

    if "a" in input_string:
        print("a found")
    else:
        print("a not found")

    if "e" in input_string:
        print("e found")
    else:
        print("e not found")

    if "o" in input_string:
        print("o found")
    else:
        print("o not found")

    if "u" in input_string:
        print("u found")
    else:
        print("u not found")

    break

string_index = input("Type a string to find the index: ")
print(string_index.find("a"))  # -1 returning which is not in the string
print(string_index.find("o"))  # on which index
print(string_index.find("e"))  # on which index

type1 = input("Type a String: ")
type2 = input("Type a specified character: ")
index = type1.find(type2)

if len(type1) > 3:
    if type2 in type1:
        print(type1[index:index+3])
    else:
        print()
else:
    print()

occurence = input("Enter the string: ")






































