#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number

# Define the square() function
def square(x):
    # Return the square of the number
    return x * x

# Call the function with one number
num = float(input("Enter a number: "))

# Get the square of the number and display it
result = square(num)
print(f"The square of {num} is: {result}")


"""Ans=>Enter a number: 6
The square of 6.0 is: 36.0"""
