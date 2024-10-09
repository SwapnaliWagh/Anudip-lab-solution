# Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.
# Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],
# 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 
# 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 
# 'age': [12, 12, 13, 13, 14, 12], 
# 'height': [173, 192, 186, 167, 151, 159], 
# 'weight': [35, 32, 33, 30, 31, 32], 
# 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Input DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Grouping the data by 'school_code' and calculating mean, min, and max of 'age' for each school
school_age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Displaying the grouped data
print("Mean, Min, and Max Age by School Code:")
print(school_age_stats)

# Plotting a horizontal bar chart based on the mean age
school_age_stats['mean'].plot(kind='barh', color='lightblue')

# Adding labels and title to the chart
plt.xlabel('Mean Age')
plt.ylabel('School Code')
plt.title('Mean Age of Students by School Code')

# Displaying the horizontal bar chart
plt.show()


# Output:

# Mean, Min, and Max Age by School Code:
#              mean  min  max
# school_code                
# s001         12.5   12   13
# s002         13.0   12   14
# s003         13.0   13   13
# s004         12.0   12   12


# Conclusion:
# By analyzing the bar chart, you can quickly observe the average age of students in each school, which can help identify whether certain schools have younger or older students on average.
# The table output also shows the minimum and maximum ages for each school, giving further insights into the age distribution across different schools.
