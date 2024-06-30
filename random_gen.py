import matplotlib.pyplot as plt
import numpy as np

# Given sets of data
data1 = [7.4732, 4.6925, 3.5395, 2.6836, 2.2876, 2.3108, 1.9676, 1.7732, 1.6228]
data2 = [3.6554, 3.1129, 2.8667, 2.2751, 1.9815, 2.1365, 1.7441, 1.4809, 1.4774]

# Generate x-values with "K (n)"
x_values = np.array([12, 18, 21, 27, 36, 42, 51, 57, 63])

# Create the plot
plt.plot(x_values, data1, marker='o', linestyle='-', color='blue', label='DLT')
plt.plot(x_values, data2, marker='o', linestyle='-', color='red', label='NDLT')

# Add title and labels with increased font size and bold text
plt.title('Errors comparison Analysis', fontdict={'fontsize': 14, 'fontweight': 'bold'})
plt.xlabel('Radar-camera pairs (K)', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('MAEE', fontdict={'fontsize': 12, 'fontweight': 'bold'})

# Add legend with increased font size and bold text
plt.legend(prop={'size': 12, 'weight': 'bold'})

# Increase numbers size in x and y axis
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the plot
plt.grid(True)
plt.show()
