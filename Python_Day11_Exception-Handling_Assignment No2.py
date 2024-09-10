#Q2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

#Function to prompt the user for an integer and manually raise ValueError if invalid
def get_integer_input():
    #Prompt the user to input a number
    user_input = input("Please enter an integer: ")
    
    #Check if the input contains only digits (positive integers)
    if not user_input.isdigit():
        #If not a valid integer, manually raise a ValueError with a custom message
        raise ValueError("ValueError:: It is an Invalid input. Please enter a valid integer.")
    else:
        #If valid, convert the input to an integer and print it
        integer_value = int(user_input)
        print(f"You entered value is a valid integer: {integer_value}")

#Try to call the function and handle any ValueError exceptions
try:
    get_integer_input()
except ValueError as e:
    #Print the error message if a ValueError occurs
    print(e)
    
"""Ans:-
Please enter an integer: Home
ValueError:: It is an Invalid input. Please enter a valid integer.

Please enter an integer: 5
You entered value is a valid integer:5"""
    