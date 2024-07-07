try:
    i = int(input("Enter the Number: "))
    c = 1 / i

except Exception as e:
    print(e)
# This finally block will be executed no matter what.
# Even if you exit() the program.
finally:
    print("We are done!")

# This block of code will only run, if there's a valid input.
print("Thanks for using the program")

