try:
    i = int(input("Enter the Number: "))
    c = 1 / i

except Exception as e:
    print(e)
# This will only run when the try block will be executed.
else:
    print("We were successfully able to divide it!")

