from collections import deque
from copy import deepcopy

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day10/data.txt'
pipes = read_data_from_file(file_path)

rows = len(pipes)
cols = len(pipes[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

grid = {}
counts = deepcopy(grid)
S = None

def get_adjacents(row, col, dirs):
    adjacents = []
    for dr, dc in dirs:
        adj_row, adj_col = row + dr, col + dc 
        if 0 <= adj_row < rows and 0 <= adj_col < cols:
            adjacent = (adj_row, adj_col)
            adjacents.append(adjacent)
    return adjacents

for i in range(rows):
    for j in range(cols):
        grid[(i, j)] = []
        adjacents = get_adjacents(i, j, directions)
        grid[(i, j)].extend(adjacents)

        if pipes[i][j] == 'S':
            S = (i, j)

pipe_connections = {
    (1, 0): ['|', 'L', 'J', 'S'],
    (-1, 0): ['7', 'F', '|', 'S'],
    (0, -1): ['-', 'F', 'L', 'S'],
    (0, 1): ['-', 'J', '7', 'S']
}

pipe_dirs = {
    '|': [(-1, 0), (1, 0)],
    '-': [(-1, 0), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (1, 0)],
    'L': [(-1, 0), (0, 1)],
}

def is_connected(node):
    row, col = node
    pipe = pipes[row][col]
    if pipe == '.':
        return False
    if pipe == 'S':
        return True
   
    for dirs in pipe_dirs[pipe]: 
        adj_pipe = get_adjacents(row, col, [dirs])
        if not any(adj_pipe):
            return False
        ax, ay = adj_pipe[0]
        pipe_type = pipes[ax][ay]
        if pipe_type not in pipe_connections[dirs]:
            return False
    return True

def bfs(graph, start):
    path = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path and is_connected(vertex):
            path.append(vertex)
            queue.extend(graph[vertex])
    return len(path)/2

print(bfs(grid, S))
        
