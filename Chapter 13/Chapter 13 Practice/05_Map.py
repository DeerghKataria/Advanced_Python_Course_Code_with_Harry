# To return sqaure of the number of a list
def square(num):
    return num * num

list1 = [1, 2, 3]
list2 = []

# This is Method 1
for item in list1:
    list2.append(square(item))

print(list2)

# This can be done in just 1 line
print(list(map(square, list1)))

# This map is used to apply this for all
# the items in the function list.