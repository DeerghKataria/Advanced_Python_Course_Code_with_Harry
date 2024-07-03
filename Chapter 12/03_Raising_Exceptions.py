def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Increment Failed!")
    
a = increment(1)
print(a)
b = increment("1f7912")
print(b)