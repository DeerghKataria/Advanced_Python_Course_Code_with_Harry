# For printing the multiplication table of a number.
# We will do this by using list compresion.
# An addition to the Problem 3 is adding.

num = int(input("Enter the Number: "))

# Printing the table
mulTable = [num * iLoop for iLoop in range(1, 11) ]
print(str(mulTable))

# Now adding all the information into tables.txt
with open("Chapter 12/Chapter 12 Practice/tables.txt", "a") as f:
    f.write(str(mulTable))