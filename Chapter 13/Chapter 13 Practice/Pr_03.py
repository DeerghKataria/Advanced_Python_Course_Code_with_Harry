# Creating a list that contains the multiplication table of the number 7.
tableSeven = [str(7 * iLoop) for iLoop in range(1, 11)]
print(tableSeven)

# Now, converting that into a vertical string list
verticalTable = "\n".join(tableSeven)
print(verticalTable)