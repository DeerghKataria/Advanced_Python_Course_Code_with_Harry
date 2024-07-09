# For dividing a/b and if b is error throw an error

def divideNumbers(a, b):
    try:
        print(f"Answer is equal to {a/b}!")

    except ZeroDivisionError:
        print("You're dividing the number by 0")

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

divideNumbers(a, b)