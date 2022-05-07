# Concatenating strings with the + operator!
# helper_string and string are different string variable.
# Everytime that we can enter any string in string, we are concatenating to helper_string.

helper_string = ""

while True:
    string = input("Enter: ")

    if string == "end":
        break
    else:
        helper_string += string + " "

print(helper_string)
