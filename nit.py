import numpy as np
import numpy as np
import numpy as np
import matplotlib.pyplot as plt


# List of .npy files
file_paths = ['distances.npy', 'distances.npy', 'gen2.npy']

# List to store the data from each file

data = []


# Read each .npy file and append the data to the list
for file_path in file_paths:
    x = np.load(file_path)
    data.append(x)
    print(sum(x)/21)
    print(min(x),max(x))


# Plot the boxplots

plt.boxplot(data)
plt.show()

# # Label the points

# for i, points in enumerate(data):
#     for j, point in enumerate(points):

#         plt.text(i+1, point, f'Point {j+1}', ha='left', va='center')

# # Calculate the mean for each dataset
# means = [np.mean(points) for points in data]

# # Plot the means
# plt.plot(range(1, len(data)+1), means, color='r', linestyle='--', label='Mean')

# # Add legend
# plt.legend()

# # Show the plot
# plt.show()