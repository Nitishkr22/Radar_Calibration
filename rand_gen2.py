import numpy as np

# Set the parameters
num_values = 21
min_value = 4.676729848157394e-03
max_value = 6.854436783759041
mean = 1.447
median = 0.82

# Generate random numbers
random_numbers = np.random.uniform(min_value, max_value, num_values)

# Adjusting mean and median
random_numbers += mean - np.mean(random_numbers)
random_numbers.sort()
random_numbers -= random_numbers[len(random_numbers) // 2] - median

print(random_numbers.shape)
print("Mean:", np.mean(random_numbers))
print("Median:", np.median(random_numbers))
np.save('gen2.npy', random_numbers)