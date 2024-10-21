import numpy as np;

# goal state for the puzzle
eight_puzzle_goal_state = np.array([[0, 1, 2],
                                    [3, 4, 5],
                                    [6, 7, 8]])



def input_eight_puzzle(): 
    two_d_list = list()
    two_d_list = []
    for i in range(3):
        row = list(map(int, input(f"Enter {i+1}-th row: ").split()))
        two_d_list.append(row)
    eight_puzzle = np.array(two_d_list)
    return eight_puzzle



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



def move_blank_piece(eight_puzzle, current_location, previous_location):
    # copy_current_location = current_location

    if np.array_equal(eight_puzzle, eight_puzzle_goal_state):
        print("Eight puzzle solved!")
        return

    new_move1 = (current_location[0]+1, current_location[1])
    new_move2 = (current_location[0]-1, current_location[1])
    new_move3 = (current_location[0], current_location[1]+1)
    new_move4 = (current_location[0], current_location[1]-1)

    probable_locations = [new_move1, new_move2, new_move3, new_move4]

    for point in probable_locations:
        copy_eight_puzzle = np.copy(eight_puzzle)
        if 0<=point[0]<3 and 0<=point[1]<3 and (point[0], point[1]) != previous_location:
            x, y = current_location[0], current_location[1]
            x_new, y_new = point[0], point[1]
            copy_eight_puzzle[x][y], copy_eight_puzzle[x_new][y_new] = copy_eight_puzzle[x_new][y_new], copy_eight_puzzle[x][y]
            move_blank_piece(copy_eight_puzzle, (x_new, y_new), (x, y))

    

# main code
eight_puzzle = input_eight_puzzle()
blank_piece_initial_location = locate_blank_piece(eight_puzzle)
move_blank_piece(eight_puzzle, blank_piece_initial_location, (-1, -1))
