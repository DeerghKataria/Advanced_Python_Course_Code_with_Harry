# For printing the multiplication table of a number.
# We will do this by using list compresion.

num = int(input("Enter the Number: "))

# Printing the table
mulTable = [num * iLoop for iLoop in range(1, 11) ]
print(mulTable)