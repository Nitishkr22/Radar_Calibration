import matplotlib.pyplot as plt

# Given data set 3
data3 = [(2.127, 6.698), (3.461, 0.811), (3.1149, 0.1180), (1.9992, 1.0732), 
         (2.0133, 0.4450), (1.887, 0.9432), (1.6126, 0.7957), (1.4168, 0.7414), 
         (1.3131, 0.6474)]

# Extract x and y values for data set 3
x_values_data3 = [pair[0] for pair in data3]
y_values_data3 = [pair[1] for pair in data3]

# Create the plot for data set 3
plt.figure(figsize=(8, 6))
plt.plot(x_values_data3, y_values_data3, marker='o', linestyle='-', color='green', label='Data Set 3')

# Add title and labels for data set 3 plot
plt.title('Plot of Data Set 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()

# Show the plot for data set 3
plt.show()
