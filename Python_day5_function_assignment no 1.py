#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

# Define the div() function
def div(a, b):
    # Perform division and return the result
    return a / b

# Call the function with two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ensure we don't divide by zero
if num2 != 0:
    result = div(num1, num2)
    print(f"The result of the division is: {result}")
else:
    print("Division by zero is not allowed.")


"""Ans=>Enter the first number: 5
Enter the second number: 3
The result of the division is: 1.6666666666666667"""
