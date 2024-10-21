import numpy as np

arr = np.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])

copy_arr = np.copy(arr)

copy_arr[2][1], copy_arr[1][2] = copy_arr[1][2], copy_arr[2][1]

print(arr)
print(copy_arr)



