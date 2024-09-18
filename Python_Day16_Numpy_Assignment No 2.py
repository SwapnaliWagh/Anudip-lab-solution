# Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
# Input: my_list = [1, 2, 3, 4, 5]

# Import the NumPy library
import numpy as np  

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the NumPy array
print("Original array:", my_array)

# Display the first and last element using indexing
first_element = my_array[0]  # Accessing the first element (index 0)
last_element = my_array[-1]  # Accessing the last element (index -1)
print("First element:", first_element)
print("Last element:", last_element)

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("Array after multiplying by 2:", multiplied_array)


"""Ans=>
Original array: [1 2 3 4 5]
First element: 1
Last element: 5
Array after multiplying by 2: [ 2  4  6  8 10] """
