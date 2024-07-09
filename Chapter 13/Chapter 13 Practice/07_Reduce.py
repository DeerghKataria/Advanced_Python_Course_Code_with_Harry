from functools import reduce

sum = lambda num1, num2: num1 + num2
list1 = [1, 2, 3, 4, 5, 6, 7]

# Now, we will use this reduce function
# to reduce the entire list to one variable

listSum = reduce(sum, list1)
print(listSum)

# In the above case, it is sequentially adding
# both numbers i.e. at index 1 and index 2 and
# similarly adding them up forwards.
