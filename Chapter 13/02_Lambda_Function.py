# Lambda function is there for the convenience of the developer.
# Rather that writing the entire function. You can just use the
# lambda keyword and create everthing a little faster.

# def func(a):
#     return a+5

# You can actually have the same functionality by using the
# lambda function, but in a single line

func = lambda a: a + 5

x = 541
print(func(x))

# Moreover in certain situation. You have to use function as an
# argument. In those specific cases, you can use this lambda
# function in your favour.

# Similarly, you can create the lambda function in the following
# ways as well. 
mult = lambda a, b: a*b
square = lambda a: a*a
subtraction = lambda a, b: a - b
addition = lambda a, b, c: a + b + c 


