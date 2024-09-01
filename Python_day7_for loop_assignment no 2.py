#Q2. Python program to check if a given number is an Armstrong number

# Take input from the user as an integer
number = int(input("Enter Your Number: "))

# Convert the number to a string 
number_str = str(number)

# Find the number of digits in the number by checking the length of the string
num_digits = len(number_str)

# Initialize a variable to store the sum of the digits raised to the power of num_digits
sum_of_powers = 0

# Iterate over each digit in the number as a string
for digit in number_str:
    # Convert the current character (digit) back to an integer
    digit = int(digit)
    # Add the digit raised to the power of num_digits to the sum
    sum_of_powers += digit ** num_digits

# Check if the calculated sum of powers is equal to the original number
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
"""ANS=> Enter Your Number: 309
         309 is not an Armstrong number.
         Enter Your Number: 407
         407 is an Armstrong number."""
