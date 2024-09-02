#2. Write a Python program to remove a newline in Python
#String = "\nBest \nDeeptech \nPython \nTraining\n"

# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines using the replace() method
cleaned_string = string.replace('\n', ' ')

# Strip leading and trailing whitespace
cleaned_string = cleaned_string.strip()

# Print the cleaned string
print(cleaned_string)


"""ANS=>Best  Deeptech  Python  Training"""


