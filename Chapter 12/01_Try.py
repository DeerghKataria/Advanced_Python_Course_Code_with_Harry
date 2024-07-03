while(True):
    print("Press 'q' to quit!")

    # Taking input for a number
    a = input("Enter a number: ")

    # For quiting the code
    if a == 'q':
        break
    
    # Converting to integer
    try:
        print("Trying....")
        a = int(a)
        if a > 6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game!")