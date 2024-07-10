# Finding the maximum within the list using reduce function
from functools import reduce

list1 = [1, 2, 3, 5, 6, 7, 23, 12, 565, 234, 15, 6, 23, 41]

a = reduce(max, list1)
# We don't need to define a function 'max' since we have this
# as an inbuilt function. Then, we can directly print
print(a)