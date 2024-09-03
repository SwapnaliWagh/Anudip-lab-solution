#1.Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve”  Output: Chars = 8 Digits = 3 Symbol = 4 

def count_characters(input_string):
    letters = digits = special_symbols = 0

    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letters += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1
        else:  # If it's neither a letter nor a digit, it's a special symbol
            special_symbols += 1

    return letters, digits, special_symbols

# Input string
input_string = "P@#yn26at^&i5ve"

# Counting letters, digits, and special symbols
letters, digits, special_symbols = count_characters(input_string)

# Printing the results
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")

"""Ans=>Letters: 8
Digits: 3
Special Symbols: 4"""
