#Q2.Compute the standard deviation of the NumPy array Input: arr = [20, 2, 7, 1, 34]

import numpy as np  #Import the NumPy library

#Input array
arr = np.array([20, 2, 7, 1, 34])  

#Compute the standard deviation of the array
#np.std() calculates the standard deviation of the array elements.
std_deviation = np.std(arr)

#Output the standard deviation of the array
print("Standard Deviation of the given  array is :", std_deviation)

"""ANS=>> Standard Deviation of the given  array is : 12.576167937809991

"""
