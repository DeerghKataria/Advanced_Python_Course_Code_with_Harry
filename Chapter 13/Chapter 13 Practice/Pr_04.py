# Filtering the numbers in a list that are divisible by 5
list1 = [1, 2, 3, 4, 5, 6, 10, 15, 17, 20, 24, 30, 35]

print(list(filter(lambda a: a % 5 == 0, list1)))