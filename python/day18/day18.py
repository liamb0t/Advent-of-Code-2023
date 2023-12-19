import copy

file_path = '2023/python/day18/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

plan = read_data_from_file(file_path)
trenches = []
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
digit_to_dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'D'}
r, c = 499, 499
grid = [['.' for j in range(1000)] for i in range(1000)]

# for line in plan:
#     dir, moves, color = line.split()[0], int(line.split()[1]), line.split()[2]
#     nr, nc = directions[dir]
  
#     for i in range(moves + 1):
#         trenches.append((r + i*nr, c + i*nc))
#         grid[r + i*nr][c + i*nc] = '#'
         
#     r += nr * moves
#     c += nc * moves

for line in plan:
    instruction = line.split()[2][2:-1]
    moves = int(instruction[:5], 16)
    dir = digit_to_dirs[instruction[-1]]

    nr, nc = directions[dir]
  
    for i in range(moves + 1):
        trenches.append((r + i*nr, c + i*nc))
        grid[r + i*nr][c + i*nc] = '#'
         
    r += nr * moves
    c += nc * moves

grid_copy = copy.deepcopy(grid)

for i in range(len(grid)):
    turns = 0
    for j in range(len(grid[0])):
    
        if grid[i][j] == '#' and (grid[i - 1][j] == '#'):
            turns += 1

        if turns % 2 != 0:
            grid_copy[i][j] = '#'

print(sum(1 for row in grid_copy for char in row if char == '#' ))

# file_path_output = '2023/python/day18/output2.txt'

# # ... (your existing code)

# # Writing grid to a text file
# with open(file_path_output, 'w') as output_file:
#     for row in grid_copy:
#         output_file.write(''.join(row) + '\n')

