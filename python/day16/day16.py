def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


file_path = '2023/python/day16/data.txt'
data = read_data_from_file(file_path)
grid = {(i, j): data[i][j]  for i in range(len(data)) for j in range(len(data[0]))}
rows = len(data)
cols = len(data[0])

elements = {
    '>': [(0, 1)],
    '<': [(0, -1)],
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '-': [(0, -1),(0, 1)],
    '|': [(-1, 0), (1, 0)],
}

def change_direction(curr_dir, elem):
    r, c = curr_dir
    if elem == '/':
        return (-c, r)
    elif elem == '\\':
        return (c, r)
    
q = [[(0, 0), (0, 1)]]
seen = []

while q:
    position, direction = q.pop(0)
    print(position, direction)
    new_position = (position[0] + direction[0], position[1] + direction[1])
    
    adjacent_elem = grid[new_position]
    
    if adjacent_elem in ['/', '\\']:
        new_direction = change_direction(direction, adjacent_elem)
    elif adjacent_elem == '.':
        new_direction = [direction]
    else:
        new_direction = elements[adjacent_elem]
    for nx, ny in new_direction:
        dx, dy = position[0] + nx, position[0] + ny
        if 0 <= dx < rows and 0 <= dy < cols:
            q.append([new_position, (nx, ny)])
            seen.append([new_position, (nx, ny)])

