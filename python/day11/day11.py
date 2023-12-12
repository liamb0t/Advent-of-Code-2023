from itertools import combinations

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day11/data.txt'
universe = [[x for x in line] for line in read_data_from_file(file_path)]
galaxies = []
rows = len(universe)
cols = len(universe[0])
empty_rows = []
empty_cols = []
expansion = 1000000 - 1

for i in range(rows):
    row = universe[i]
    col = []
    if all(x=='.' for x in row):
        empty_rows.append(i)
    for j in range(cols): 
        col.append(universe[j][i])
        if universe[i][j] == '#':
            galaxies.append((i, j))
    if all(x=='.' for x in col):
        empty_cols.append(i)

def move_galaxy(node):
    row, col = node[0], node[1]
    for empty_row in empty_rows[::-1]:
        if node[0] > empty_row:
            row = node[0] + ((empty_rows.index(empty_row) + 1) * expansion)
            break
    for empty_col in empty_cols[::-1]:
        if node[1] > empty_col:
            col = node[1] + ((empty_cols.index(empty_col) + 1) * expansion)
            break
    return (row, col)

shifted_galaxies = list(map(move_galaxy, galaxies))
num_galaxies = len(galaxies)
total = 0

for p1, p2 in combinations(shifted_galaxies, 2):
    x1, y1 = p1
    x2, y2 = p2
    total += abs(x1 - x2) + abs(y1 - y2)

print(total)