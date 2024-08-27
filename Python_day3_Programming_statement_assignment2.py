# Using input function take two number and then swap the number

# Take two numbers as input from the user

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Display original numbers
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers
num1, num2 = num2, num1

# Display swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")

"""Enter the first number: 2 10
Enter the second number: 15 5
Before swapping: num1 = 2 10, num2 = 15 5
After swapping: num1 = 15 5, num2 = 2 10"""
