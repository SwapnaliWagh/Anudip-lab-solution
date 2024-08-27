#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number is {result}.")

"""ANS:-Enter a number: 3
The number is Odd
Enter a number: 10
The number is Even."""
