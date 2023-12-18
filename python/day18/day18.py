file_path = '2023/python/day18/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

plan = read_data_from_file(file_path)
trenches = []
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
r, c = 499, 499
grid = [['.' for j in range(1000)] for i in range(1000)]

for line in plan:
    dir, moves, color = line.split()[0], int(line.split()[1]), line.split()[2]
    nr, nc = directions[dir]
  
    for i in range(moves + 1):
        trenches.append((r + i*nr, c) if nr != 0 else (r, c + i*nc))
        grid[r + i*nr if nr != 0 else r][c if nr != 0 else c + i*nc] = '#'
         
    r += nr * moves
    c += nc * moves



for i, row in enumerate(grid):
    counter = 0
    for j, char in enumerate(row):

        if counter % 2 != 0 and not all(x == '.' for x in row[j:]):
            grid[i][j] = '#'

        try:
            if (grid[i][j] == '.' and grid[i][j + 1] == '#') or (grid[i][j] == '#' and grid[i][j + 1] != '.'):
                counter += 1
        except:
            pass
      


print(sum(1 for row in grid for char in row if char == '#' ))

file_path_output = '2023/python/day18/output2.txt'

# ... (your existing code)

# Writing grid to a text file
with open(file_path_output, 'w') as output_file:
    for row in grid:
        output_file.write(''.join(row) + '\n')

