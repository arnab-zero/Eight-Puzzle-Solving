import numpy as np
from collections import deque

eight_puzzle_goal_state = np.array([[0, 1, 2],
                                    [3, 4, 5],
                                    [6, 7, 8]])

eight_puzzle = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]])

eight_puzzle_v1 = np.array([[1, 2, 3],
                         [4, 5, 0],
                         [7, 8, 6]])

visitedVariations.add(tuple(eight_puzzle.flatten()))
visitedVariations.add(tuple(eight_puzzle_v1.flatten()))

newVariations.append(eight_puzzle)
newVariations.append(eight_puzzle_v1)

if tuple(eight_puzzle.flatten()) in visitedVariations:
    print("Eight puzzle variation visited already.")

print("Set:", visitedVariations)
print("Deque:", newVariations)

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


visitedVariations = set({})
newVariations = deque([]) 

newVariations.append(eight_puzzle)

# def move_blank_piece(eight_puzzle, current_location, previous_location):
#     # copy_current_location = current_location
#     # copy_eight_puzzle = eight_puzzle

#     while newVariations:

#         current_variation = newVariations.popleft()

#         if np.array_equal(eight_puzzle, eight_puzzle_goal_state):
#             print("Eight puzzle solved!")
#             return
        
#         new_move1 = (current_location[0]+1, current_location[1])
#         new_move2 = (current_location[0]-1, current_location[1])
#         new_move3 = (current_location[0], current_location[1]+1)
#         new_move4 = (current_location[0], current_location[1]-1)

#         probable_locations = [new_move1, new_move2, new_move3, new_move4]

#         # problem here
#         for point in probable_locations: 
#             copy_eight_puzzle = np.copy(eight_puzzle)
#             if 0<=point[0]<3 and 0<=point[1]<3 and (point[0], point[1]) != previous_location:
#                 x, y = current_location[0], current_location[1]
#                 x_new, y_new = point[0], point[1]
#                 print(x, y, x_new, y_new)
#                 copy_eight_puzzle[x][y], copy_eight_puzzle[x_new][y_new] = copy_eight_puzzle[x_new][y_new], copy_eight_puzzle[x][y]
#                 print(eight_puzzle)
#                 print(copy_eight_puzzle)
#                 print((x, y))
#                 print((x_new, y_new))
#                 move_blank_piece(copy_eight_puzzle, (x_new, y_new), (x, y))


# main code
# blank_piece_location = locate_blank_piece(eight_puzzle)
# print(blank_piece_location)
# move_blank_piece(eight_puzzle, blank_piece_location, (-1, -1))
