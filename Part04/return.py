def my_sum(a, b):
    return a + b

result = my_sum(2, 3)
print("Sum:", result)

def ask_for_name():
    ask_name = input("What is your name? ")
    return ask_name

name = ask_for_name()
print("Hello there,", name)

def smallest(a, b):
    if a < b:
        return a
    return b
print(smallest(7, 19))
print(smallest(19, 1))

def greet(name):
    if name == "":
        print("???")
        return
    print("Hello there,", name)
greet("Jack")
greet("")
greet("Mark")