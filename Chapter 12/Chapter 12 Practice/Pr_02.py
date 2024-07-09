# For printing the third, fifth and seventh element of a list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, elem in enumerate(list1):
    if index == 2:
        print(f"Element {index+1}rd is {elem}")
    elif index == 4:
        print(f"Element {index+1}th is {elem}")
    elif index == 6:
        print(f"Element {index+1}th is {elem}")
    