#Q1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.#

#Function to divide two numbers with exception handling
def divide_numbers():
    try:
        #Taking input from the user for the numerator and converting it to a float
        numerator = float(input("Enter the numerator: "))
        
        #Taking input from the user for the denominator and converting it to a float
        denominator = float(input("Enter the denominator: "))
        
        #Attempt the division operation
        result = numerator / denominator  # This may raise a ZeroDivisionError
        
        #If no error occurs, print the result of the division
        print(f"The result of {numerator} divided by {denominator} is: {result}")
    
    except ZeroDivisionError:
        #This block executes if a ZeroDivisionError occurs (denominator is zero)
        #It prints an error message, preventing the program from crashing
        print("ZeroDivisionError:: You cannot divide by zero. Please try again with a valid denominator.")
    
    except ValueError:
        #This block executes if the input cannot be converted to a float
        #It prints an error message, asking for valid numeric input
        print("ValueError:: Please enter a valid number for both numerator and denominator.")

#Call the function to execute the program
divide_numbers()

"""Ans:-
Enter the numerator: 20
Enter the denominator: 0
ZeroDivisionError:: You cannot divide by zero. Please try again with a valid denominator.

Enter the numerator: 30
Enter the denominator:15
The result of 30.0 divided by 15.0 is: 2.0 """