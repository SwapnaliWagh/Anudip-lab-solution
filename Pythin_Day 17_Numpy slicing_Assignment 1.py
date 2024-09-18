#Q.1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np  # Import the NumPy library

#Create an array of 10 zeros
zeros_array = np.zeros(10)  #np.zeros() creates an array filled with zeros
print("Array of 10 zeros:", zeros_array) #Print the array of zeros

#Create an array of 10 ones
ones_array = np.ones(10)  #np.ones() creates an array filled with ones
print("Array of 10 ones:", ones_array)  #Print the array of ones

#Create an array of 10 fives
fives_array = np.full(10, 5)  # np.full() creates an array filled with a specified value, here 5
print("Array of 10 fives:", fives_array)  #Print the array of fives


"""ANS=> Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
          Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
          Array of 10 fives: [5 5 5 5 5 5 5 5 5 5] """
