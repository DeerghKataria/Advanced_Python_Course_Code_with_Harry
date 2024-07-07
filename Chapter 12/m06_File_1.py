def greet(name):
    print(f"Good morning, {name}")

# It will print the name of the file.
# print(__name__)

# It will only run when you run the same file.
if __name__ == "__main__":
    n = input("What's your name?\n")
    greet(n)
