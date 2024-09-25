#Q1. Install matplotlib  & you can use plt.plot() to create a line plot of given data ,x = [0, 5, 9, 10, 15, 20, 25] ,y = [0, 1, 2, 3, 4, 5, 6]
#Solution=>>
#Importing the matplotlib library's pyplot module
import matplotlib.pyplot as plt

x = [0, 5, 9, 10, 15, 20, 25]  # X-axis values
y = [0, 1, 2, 3, 4, 5, 6]      # Y-axis values

#Creating a line plot with the provided x and y values
plt.plot(x, y , marker='o' , linestyle='-', color='b')

#Adding a title to the plot to describe it
plt.title("Line Plot with Markers")

#Labeling the X-axis
plt.xlabel("X-axis")

#Labeling the Y-axis
plt.ylabel("Y-axis")

#Displaying the plot to the screen
plt.show()  
