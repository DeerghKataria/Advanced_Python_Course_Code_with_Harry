def greaterThan5(num):
    if num > 5:
        return True
    else:
        return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Now, this will return all the numbers in the
# list that are greater than 5.
print(list(filter(greaterThan5, list1)))


# Now, you can also write this by using the lambda
# function that we learned earlier.

greaterThan10 = lambda num: num > 10
print(list(filter(greaterThan10, list1)))