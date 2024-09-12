#2.Write a Python script to concatenate the following dictionaries to create a new one. 
#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define the dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries
new_dict = {}
for d in (dic1, dic2, dic3):
    new_dict.update(d)

# Print the result
print("Concatenated dictionary:", new_dict)

"""Ans=>
Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""