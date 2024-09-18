Q.2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np  #Import the NumPy library

#Create an array with values from 2 to 10
#Use np.arange(start, stop) to generate numbers from 2 to 10 The stop value is 11 because the end value is exclusive in np.arange
values_array = np.arange(2, 11)  #This creates an array: [2, 3, 4, 5, 6, 7, 8, 9, 10]

#Reshape the array into a 3x3 matrix
#Use np.reshape() to change the shape of the array to 3 rows and 3 columns
matrix_3x3 = np.reshape(values_array, (3, 3))  #This reshapes it into a 3x3 matrix

#Print the 3x3 matrix
print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix_3x3)

"""ANS=>
3x3 Matrix with values ranging from 2 to 10:
[[ 2  3  4]
[ 5  6  7]
[ 8  9 10]]
"""
