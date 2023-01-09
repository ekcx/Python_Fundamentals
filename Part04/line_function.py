def function(line1, line2):
    line1 = input("Type something: ")
    line2 = input("Type another thing:")
    print(line1 + " " + line2)

line_two, line_one = " ", " "
function(line_one, line_two)

def line(number, char):
    if char == "":
        print(number * "*")
    else:
        print(number * char)

line(7, "%")
line(10, "LOL")
line(3, "")

def greet(name):
    print("Hello there,", name)

def greet_many_times(name, times):
    while times > 0:
        greet(name)
        times -= 1

greet_many_times("Emily", 5)