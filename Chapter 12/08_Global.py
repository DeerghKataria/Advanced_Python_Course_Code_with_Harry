a = 54      # Global variable

def func1():
    # By using this global keyword, the value of global 'a'
    # be changed permanently.
    global a
    print(a)

    # If the global keyword would not have been mentioned
    # then another local variable 'a' would have been created.

    a = 8   # Local variable
    print(a)

func1()
print(a)