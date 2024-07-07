a  = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]

# Let's say we want to consider only the even
# items in this list. Then,

# b = []

# for item in a:
#     if item % 2 == 0:
#         b.append(item)

# print(b)

# Rather than typing the above code, you can do it directly
# using the following:

b = [item for item in a if item % 2 == 0]
print(f"List comprehension {b}")


# The same thing can be done with set as well
t = [1, 4, 2, 4, 1, 2, 8]
s = {items for items in t}
print(f"Set comprehension {s}")