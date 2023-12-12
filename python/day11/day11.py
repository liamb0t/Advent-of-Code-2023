def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day11/data.txt'
universe = [[x for x in line] for line in read_data_from_file(file_path)]
galaxies = {}
rows = len(universe)
cols = len(universe[0])
empty_rows = []
empty_cols = []
galaxy_num = 1

for i in range(rows):
    row = universe[i]
    col = []
    if all(x=='.' for x in row):
        empty_rows.append(i)
    for j in range(cols): 
        col.append(universe[j][i])
        if universe[i][j] == '#':
            galaxies[galaxy_num] = (i, j)
            galaxy_num += 1
    if all(x=='.' for x in col):
        empty_cols.append(i)

def move_galaxy(node):
    row, col = node[0], node[1]
    for empty_row in empty_rows:
        if node[0] > empty_row:
            row = node[0] + empty_rows.index(empty_row) + 1
    for empty_col in empty_cols:
        if node[1] > empty_col:
            col = node[1] + empty_cols.index(empty_col) + 1
    return (row, col)

shifted_galaxies = {}
for i, coords in  enumerate(list(map(move_galaxy, galaxies.values())), 1):
    shifted_galaxies[i] = coords

num_galaxies = len(galaxies.keys())
sum = 0

for i in range(1, num_galaxies + 1):
    for j in range(i, num_galaxies + 1):
        if i != j:
            x1, y1 = shifted_galaxies[i]
            x2, y2 = shifted_galaxies[j]
            sum += abs(x2 - x1) + abs(y2 - y1)
            
print(sum)