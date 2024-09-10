# Write a Python program to get the largest and smallest number from a list without builtin functions. 

# Define a function to find the largest and smallest numbers in a list
def find_largest_and_smallest(numbers):
    # Assume the first number is both the largest and the smallest
    largest = numbers[0]
    smallest = numbers[0]

    # Iterate over each number in the list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the largest, update largest
        if num > largest:
            largest = num
        # If the current number is smaller than the smallest, update smallest
        if num < smallest:
            smallest = num

    return largest, smallest  # Return both largest and smallest numbers

# Example list
my_list = [11, 22, 18,2, 32, 20]

# Call the function and store the results
largest, smallest = find_largest_and_smallest(my_list)

# Print the results
print("The largest number is:", largest)
print("The smallest number is:", smallest)


"""Ans=>
The largest number is: 32
The smallest number is: 2
"""