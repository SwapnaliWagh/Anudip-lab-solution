#Q1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] # Monthly expenses in dollars (replace with your own data) expenses = [1200, 400, 200, 150, 250]
#Solution=>>

import matplotlib.pyplot as plt   #Importing the Matplotlib library for plotting

#Input data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

#Create a bar chart with 'categories' on x-axis and 'expenses' on y-axis, using a light blue color for bars
plt.bar(categories, expenses, color='lightblue')  

#Adding labels and title
plt.xlabel('Spending Categories')
plt.ylabel('Monthly Expenses ($)')
plt.title('Monthly Expenses by Category')


#Render and display the bar chart
plt.show()
