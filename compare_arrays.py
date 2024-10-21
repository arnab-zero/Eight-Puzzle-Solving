import numpy as np

# Array 1
array_2d_0 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]])

# Array 2
array_2d_1 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Array 3
array_2d_2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]])

print(f"Array-1 and Array-2 are {"" if np.array_equal(array_2d_0, array_2d_1) else "not "}equal.")
print(f"Array-1 and Array-3 are {"" if np.array_equal(array_2d_0, array_2d_2) else "not "}equal.")
