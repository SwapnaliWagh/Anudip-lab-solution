#Q1.Python program to check if the given string is a palindrome 
#Take input from the user
number = input("Enter a number: ")

#Initialize a variable to assume the number matches the palindrome condition
is_palindrome = True

#Iterate through each character up to the midpoint of the string for comparison
for i in range(len(number) // 2):
    
#Compare the digit at position i from the start with the corresponding digit from the end
    if number[i] != number[-i - 1]:
        is_palindrome = False         #If digits don't match, set the variable to False
        break  #Exit the loop if a mismatch is found

#After the loop, check if the variable is still True
if is_palindrome:
    print("The number is a palindrome.")    
else:
    print("The number is not a palindrome.")     
"""ANS=> Enter a number: 32123
          The number is a palindrome.
          Enter a number: 324
          The number is not a palindrome.
 """
