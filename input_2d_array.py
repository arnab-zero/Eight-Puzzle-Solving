import numpy as np;

def input_eight_puzzle_initial_state(): 
    two_d_list = list()
    two_d_list = []
    for i in range(3):
        row = list(map(int, input(f"Enter {i+1}-th row: ").split()))
        two_d_list.append(row)
    two_d_array = np.array(two_d_list)
    return two_d_array

array_2d = input_eight_puzzle_initial_state()
print("Printing the 2-d array:")
print(array_2d)
    
