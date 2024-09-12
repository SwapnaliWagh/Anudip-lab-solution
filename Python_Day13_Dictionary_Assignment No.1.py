#1.Write a Python program and calculate the mean of the below dictionary.
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 
#Output: 6.2

# Define the dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean of the values
mean_value = sum(test_dict.values()) / len(test_dict)

# Print the result
print(f"The mean of the values in the dictionary is: {mean_value}")


"""Ans=>
The mean of the values in the dictionary is: 6.2"""
