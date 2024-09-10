# Write a Python program to find duplicate values from a list and display those

# Define a function to find and display duplicate values in a list
def find_duplicates(numbers):
    duplicates = []  # List to store the duplicates
    checked = []  # List to store the already checked numbers

    # Iterate through each number in the list
    for num in numbers:
        # If the number has already been checked and is not in duplicates, it's a duplicate
        if num in checked and num not in duplicates:
            duplicates.append(num)
        else:
            # Otherwise, add the number to the checked list
            checked.append(num)

    return duplicates  # Return the list of duplicates

# Example list
my_list = [2, 5, 2, 5, 7, 2, 7, 1, ]

# Call the function and store the result
duplicate_values = find_duplicates(my_list)

# Print the duplicate values
print("The duplicate values are:", duplicate_values)

"""Ans=>
The duplicate values are: [2, 5]
"""