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
empty_rows = [i for i, row in enumerate(universe) if all(cell == '.' for cell in row)]
empty_cols = [i for i in range(cols) if all(row[i] == '.' for row in universe)]
galaxies = [(i, j) for i in range(rows) for j in range(cols) if universe[i][j] == '#']

expansion = 1000000 - 1

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
total = sum([abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in combinations(shifted_galaxies, 2)])

print(total)