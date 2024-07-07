list1 = [3, 53, 2, False, 6.2, "Deergh"]

# index = 0
# for item in list1:
#     print(item, index)
#     index = index + 1

# In case, if you don't want to manually take
# the index into consideration then you can use
# enumerate function.

for index, item in enumerate(list1):
    print(index, item)

# The above way reduces our work and we don't have
# to calculate the index all of that work is done itself.