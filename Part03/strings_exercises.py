import math

get_string = input("Word")
print("*" * 30)
print("*" * 1 + " " * math.floor((28 - math.floor(len(get_string)))/2) + get_string + " " * math.floor((28 - math.floor(len(get_string)))/2) + 1 * "*")

# String slicing string[start:end]

string = "Exemplary"
if string[2:6] == "empl":
    print(True)
else:
    print(False)

print(string[:5])  # starting default 0
print(string[3:])  # ending default 0

