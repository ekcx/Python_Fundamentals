
main_string = input("Enter the string: ")
occurence_string = input("Enter the substring: ")
string_check = 0

while True:
    if occurence_string in main_string:
        string_check = 1

    if main_string.find(occurence_string) != -1 and string_check == 1:
        print(main_string.find(string_check))
    else:
        print("The second occurence of the substring is not here.")