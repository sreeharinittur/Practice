def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)//recursive function call

print(factorial(5))
