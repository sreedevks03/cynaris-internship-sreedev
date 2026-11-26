
import numpy as np

# 1. Broadcasting
numbers = np.array([10, 20, 30, 40])
result = numbers + 5

print("Broadcasting:", result)

# 2. Vectorised operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

addition = a + b
multiplication = a * b
division = b / a

print("\nAddition:", addition)
print("Multiplication:", multiplication)
print("Division:", division)

# 3. Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result_matrix = matrix_a @ matrix_b

print("\nMatrix Multiplication:")
print(result_matrix)
