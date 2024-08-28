#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate 5 random numbers and store them in a list
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the random numbers
print("Random numbers:", random_numbers)

# Find and display the maximum and minimum values
max_value = max(random_numbers)
min_value = min(random_numbers)

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")

"""Ans=>Random numbers: [81, 7, 6, 97, 5]
The maximum value is: 97
The minimum value is: 5"""

