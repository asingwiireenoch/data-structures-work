import numpy as np

# Create a NumPy array with the values 1, 7, 13, 105
array = np.array([1, 7, 13, 105])

# Get the size of the memory occupied by the array
size_in_bytes = array.nbytes

# Print the array and its memory size
print("Array:", array)
print("Size in bytes:", size_in_bytes, "bytes")