from collections import deque

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day11/data.txt'
universe = [[x for x in line] for line in read_data_from_file(file_path)]
galaxies = {}
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_adjacents(row, col, dirs):
    adjacents = []
    for dr, dc in dirs:
        adj_row, adj_col = row + dr, col + dc 
        if 0 <= adj_row < rows and 0 <= adj_col < cols:
            adjacent = (adj_row, adj_col)
            adjacents.append(adjacent)
    return adjacents

rows = len(universe)
cols = len(universe[0])
empty_rows = []
empty_cols = []

def is_empty_row(row):
    return True if all(x=='.' for x in row) else False

def is_empty_col(col):
    return True if all(x=='.' for x in col) else False

galaxy_num = 1

for i in range(rows):
    row = universe[i]
    col = []
    if is_empty_row(row):
        empty_rows.append(i)
    for j in range(cols): 
        col.append(universe[j][i])
        if universe[i][j] == '#':
            galaxies[galaxy_num] = (i, j)
            galaxy_num += 1
    if is_empty_col(col):
        empty_cols.append(i)

def move_galaxy(node):
    row, col = node[0], node[1]
    for empty_row, empty_col in zip(empty_rows, empty_cols):
        if node[0] > empty_row:
            row = node[0] + empty_rows.index(empty_row) + 1
        if node[1] > empty_col:
            col = node[1] + empty_cols.index(empty_col) + 1
    return (row, col)

shifted_galaxies = {}
for i, coords in  enumerate(list(map(move_galaxy, galaxies.values())), 1):
    shifted_galaxies[i] = coords

graph = {}

for i in range(rows + len(empty_rows)):
    for j in range(cols + len(empty_cols)):
        graph[(i, j)] = get_adjacents(i, j, directions)

num_galaxies = len(galaxies.keys())
sum = 0

def bfs(start, end):
    queue = deque([(start, 0)])
    seen = set()
    while queue:
        node, distance = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        if node == end:
            return distance
        for adjacent in graph.get(node, []):
            queue.append((adjacent, distance + 1))

# for i in range(1, num_galaxies + 1):
#     for j in range(i, num_galaxies + 1):
#         if i != j:
#             start = shifted_galaxies[i]
#             end = shifted_galaxies[j]
#             sum += bfs(start, end)

start = shifted_galaxies[1]
end = shifted_galaxies[9]

print(bfs(start, end))