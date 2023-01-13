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

def greatest_number(number1, number2, number3):
    if number1 >= number2 >= number3:
        return print(number1)
    elif number2 >= number3 >= number1:
        return print(number2)
    elif number3 >= number2 >= number1:
        return print(number3)

greatest_number(13,13,13)
greatest_number(5,12,11)
greatest_number(12,10,0)

def same_chars(my_string, index1, index2):
    if index1 > len(my_string) or index2 > len(my_string):
        return print(False)
    elif my_string[index1] == my_string[index2]:
        return print(True)

same_chars("programmer", 6, 7)
same_chars("programmer", 0, 4)
same_chars("programmer", 0, 12)