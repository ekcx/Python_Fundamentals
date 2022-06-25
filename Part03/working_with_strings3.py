# Character Occurence Control
import gettext

main_string = input("Type in a string: ")
occurence_character = input("Type in a character: ")
string_check = 0

for i in main_string:
    if i == occurence_character:
        string_check = string_check + 1

print(string_check)

# The Second Occurence

occurence = input("Please enter the string: ")
substring = input("Type a substring: ")

firstText = occurence.find(substring)

if occurence.find(substring, firstText + 1) != -1:
    print("The second occurence of the substring is at index", occurence.find(substring, firstText + 1))
else:
    print("The string has no second substring.")
