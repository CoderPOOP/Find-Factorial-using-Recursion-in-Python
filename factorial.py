# Factorial using Recursion in Python

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))

num = input("Enter the Number: ")
print(factorial(int(num)))