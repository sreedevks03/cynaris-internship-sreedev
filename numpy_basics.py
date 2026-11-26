
import numpy as np
array_1d = np.array([10, 20, 30, 40])
array_2d = np.array([[1, 2, 3],[4, 5, 6]])
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("1D Array:", array_1d)
print("1D Shape:", array_1d.shape)

print("\n2D Array:\n", array_2d)
print("2D Shape:", array_2d.shape)

print("\n3D Array:\n", array_3d)
print("3D Shape:", array_3d.shape)

# Check dimensions and total elements
print("\nDimensions:", array_1d.ndim, array_2d.ndim, array_3d.ndim)
print("Total elements:", array_1d.size, array_2d.size, array_3d.size)
