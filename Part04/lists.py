my_list = []
my_list.append(5)
my_list.append(10)
print(my_list)
print(len(my_list))

change_value = [1, 2, 3, 4, 5]
index = 0
new_value = 0

while (True):
    index = int(input("Index:"))
    if index == -1:
        break
    new_value = int(input("New Value:"))
    change_value[index] = new_value
    print(change_value)

numbers = []
numbers.append(3)
numbers.append(10)
numbers.append(5)
print(numbers)

# Adding to the specific location #

points = [10, 9, 10, 8, 7, 7, 10 ,7]
# insert puts the number to the specified index!
points.insert(2, 12)    # 2 is the index
print(points)
points.insert(0, 11)    # 0 is the index
print(points)