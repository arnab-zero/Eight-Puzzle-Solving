import numpy as np
from collections import deque

# initializations
eight_puzzle_goal_state = np.array([[0, 1, 2],
                                    [3, 4, 5],
                                    [6, 7, 8]])

eight_puzzle = np.array([[1, 4, 2],
                         [0, 3, 5],
                         [6, 7, 8]])

visitedVariations = set({})
pendingVariations = deque([]) 

def input_eight_puzzle_initial_state(): 
    two_d_list = list()
    two_d_list = []
    for i in range(3):
        row = list(map(int, input(f"Enter {i+1}-th row: ").split()))
        two_d_list.append(row)
    two_d_array = np.array(two_d_list)
    return two_d_array

def locate_blank_piece(eight_puzzle):
    location = (1, 1);

    if eight_puzzle[0][0]==0:
        location = (0, 0)
    elif eight_puzzle[0][2]==0:
        location = (0, 2)
    elif eight_puzzle[2][0]==0:
        location = (2, 0)
    elif eight_puzzle[2][2]==0:
        location = (2, 2)
    elif eight_puzzle[0][1]==0:
        location = (0, 1)
    elif eight_puzzle[1][0]==0:
        location = (1, 0)
    elif eight_puzzle[1][2]==0:
        location = (1, 2)
    elif eight_puzzle[2][1]==0:
        location = (2, 1)

    return location

# solve this shit
def move_blank_piece():

    i = 0

    while len(pendingVariations):
        i = i+1
        step = f"====================== Step-{i} ======================"
        print(step)

        if len(pendingVariations) == 0 :
            exit()

        currentVariation = pendingVariations.popleft()
        visitedVariations.add(tuple(currentVariation.flatten()))

        print("Current variation: ", currentVariation)
        
        if np.array_equal(currentVariation, eight_puzzle_goal_state):
            print("Eight puzzle solved!")
            exit()

        current_location = locate_blank_piece(currentVariation)
        
        new_move1 = (current_location[0]+1, current_location[1])
        new_move2 = (current_location[0]-1, current_location[1])
        new_move3 = (current_location[0], current_location[1]+1)
        new_move4 = (current_location[0], current_location[1]-1)

        probable_locations = [new_move1, new_move2, new_move3, new_move4]

        for point in probable_locations: 
            copy_current_variation = np.copy(currentVariation)
            # print("Sub-step")
            if 0<=point[0]<3 and 0<=point[1]<3:  ##  and (point[0], point[1]) != previous_location
                x, y = current_location[0], current_location[1]
                x_new, y_new = point[0], point[1]
                copy_current_variation[x][y], copy_current_variation[x_new][y_new] = copy_current_variation[x_new][y_new], copy_current_variation[x][y]
                # print(copy_current_variation)
                if tuple(copy_current_variation.flatten()) not in visitedVariations:
                    pendingVariations.append(copy_current_variation)
        
    print("Eight puzzle can't be solved from the given initial state.")



## Main
# eight_puzzle = input_eight_puzzle_initial_state()
# eight_puzzle = np.array([[3, 0, 2], 
#                          [6, 1, 4], 
#                          [7, 8, 5]])

# eight_puzzle = np.array([[1, 0, 2],           ## Solved
#                          [6, 3, 4], 
#                          [7, 5, 8]])

# eight_puzzle = np.array([[1, 0, 2],           
#                          [8, 3, 4], 
#                          [7, 5, 6]])

# eight_puzzle = np.array([[0, 1, 2],           
#                          [8, 3, 4], 
#                          [7, 5, 6]])

eight_puzzle = np.array([[1, 2, 5],
          [3, 4, 7],
          [6, 8, 0]])



pendingVariations.append(eight_puzzle)
move_blank_piece()
