import numpy as np

# Create a NumPy array with mixed data types
array = np.array([1, 2.5, 3 + 4j, 5, 6.2, 7, 8 + 9j])

# Test if each element is complex
is_complex = np.iscomplex(array)

# Test if each element is real
is_real = np.isreal(array)

# Test if a given number is of a scalar type
number = 42
is_scalar = np.isscalar(number)

# Print the results
print("Array:", array)
print("Is complex:", is_complex)
print("Is real:", is_real)
print("Is", number, "a scalar:", is_scalar)