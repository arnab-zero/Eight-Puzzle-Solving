import numpy as np
import copy

goal_state = np.array([[0, 1, 2], 
                       [3, 4, 5], 
                       [6, 7, 8]])

moves = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

def input_eight_puzzle_initial_state(): 
    two_d_list = list()
    two_d_list = []
    print("\nEight puzzle initial state input:")
    for i in range(3):
        row = list(map(int, input(f"Enter {i+1}-th row: ").split()))
        two_d_list.append(row)
    print("\n")
    two_d_array = np.array(two_d_list)
    return two_d_array

def find_blank_piece_location(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return np.array_equal(state, goal_state)

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Move blank piece to find next valid arrangement of 8-puzzle
def move_blank_piece(state):
    blank_x, blank_y = find_blank_piece_location(state)
    next_states = []
    
    for move_name, (dx, dy) in moves.items():
        new_x, new_y = blank_x + dx, blank_y + dy
        if is_valid_move(new_x, new_y):
            new_state = copy.deepcopy(state)
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            next_states.append((new_state, move_name))
    
    return next_states

def is_solvable(state):
    flattened = state.flatten()
    inv_count = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if flattened[i] != 0 and flattened[j] != 0 and flattened[i] > flattened[j]:
                inv_count += 1
    return inv_count % 2 == 0

def dls(state, depth, path):
    if is_goal(state):
        return path
    
    if depth == 0:
        return None
    
    next_states = move_blank_piece(state)
    
    for next_state, move_name in next_states:
        if any(np.array_equal(next_state, visited_state) for visited_state, _ in path):  
            continue
        new_path = path + [(next_state, move_name)]
        result = dls(next_state, depth - 1, new_path)
        if result:
            return result
    
    return None

def iddfs(initial_state, max_depth):
    print("Searching the goal state: ")
    for depth in range(max_depth + 1):
        print(f"---> Exploring depth level - {depth} ")
        path = dls(initial_state, depth, [(initial_state, 'initial position')])
        if path:
            return path
    print("\n")
    return None

# Prints the moves made to reach goal state
def display_solution(path):
    print("\nHow we solved the eight puzzle: ")
    for i, (state, move_name) in enumerate(path):
        print(f"Move {i}: Blank piece to the {move_name}")
        print(state)

def solve_8_puzzle(initial_state, max_depth=25):
    if not is_solvable(initial_state):
        print("\n8-puzzle cannot be solved")
        return
    
    solution = iddfs(initial_state, max_depth)
    
    if solution:
        display_solution(solution)
    else:
        print("8-puzzle cannot be solved within depth limit")



### Main
initial_state = input_eight_puzzle_initial_state()
solve_8_puzzle(initial_state)
