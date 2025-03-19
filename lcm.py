import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)

# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Calculate LCM
result = lcm_three(num1, num2, num3)//calling the function

# Display the result
print("LCM of", num1, ",", num2, "and", num3, "is:", result)
