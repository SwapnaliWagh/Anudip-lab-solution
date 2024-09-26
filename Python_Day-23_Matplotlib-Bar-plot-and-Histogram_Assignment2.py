#2.Visualize the daily temperature changes over time in a city and give your conclusion  ,Input: days = list(range(1, 32)) # Daily temperature data (replace with your own data) ,temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
#Solution=>>

#Importing the Matplotlib library to create visualizations
import matplotlib.pyplot as plt

#Input data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

#Plot days on the x-axis and temperature on the y-axis, using darkgreen solid line with circular markers and customized thickness and size.
plt.plot(days, temperature, marker='o', color='darkgreen', linestyle='-', linewidth=2, markersize=5)

# Adding labels and title
plt.xlabel('Days of the Month')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperature Changes Over Time')

#renders and displays the line plot
plt.show()
