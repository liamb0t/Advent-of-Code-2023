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
S = None

valid_connections = {
    (1, 0): ['|', 'L', 'J', 'S'],
    (-1, 0): ['7', 'F', '|', 'S'],
    (0, -1): ['-', 'F', 'L', 'S'],
    (0, 1): ['-', 'J', '7', 'S']
}

pipe_dirs = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, 1), (0, -1)],
    'F': [(1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'L': [(-1, 0), (0, 1)],
}

def get_connections(node):
    connections = []
    row, col = node
    pipe = pipes[row][col]
    
    if pipe == '.':
        return None
    if pipe == 'S':
        return None
   
    for dirs in pipe_dirs[pipe]: 
        adj_pipe = get_adjacents(row, col, [dirs])
        if not any(adj_pipe):
            return False
        ax, ay = adj_pipe[0]
        pipe_type = pipes[ax][ay]
        if pipe_type not in valid_connections[dirs]:
            return None
        else:
            connections.extend(adj_pipe)
    return connections

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
        connections = get_connections((i, j))
        if connections:
            grid[(i, j)].extend(connections)
        if pipes[i][j] == 'S':
            S = (i, j)

def bfs(graph, start):
    path = []
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)
            queue.extend(graph[vertex])
    return len(path)/2


print(bfs(grid, (54, 15)))