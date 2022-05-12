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
