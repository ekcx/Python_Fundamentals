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

# [a:b] is half-open, a included, b excluded

get_string = input("Type in a string:")
lenght = len(get_string)

for i in range(0, lenght):
    print(get_string[i:lenght])

for i in range(lenght, -1, -1):
    print(get_string[i:lenght])

for i in range(0, lenght):
    print(get_string[0:i+1])

