def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day16/data.txt'
data = read_data_from_file(file_path)
grid = {(i, j): data[i][j]  for i in range(len(data)) for j in range(len(data[0]))}
rows = len(data)
cols = len(data[0])

def handle_mirror(curr_dir, elem):
    r, c = curr_dir
    if elem == '/':
        return [(-c, -r)]
    elif elem == '\\':
        return [(c, r)]
    
def handle_breaker(curr_dir, new_pos, elem, dir):
    if elem == '|':
        if curr_dir[1] == new_pos[1]:
            return [dir]
        else:
            return [(-1, 0), (1, 0)]
    if elem == '-':
        if curr_dir[0] == new_pos[0]:
            return [dir]
        else:
            return [(0, -1),(0, 1)]
   
q = [[(0, 0), (1, 0)]]
seen = [q[0]]

while q:
    position, direction = q.pop(0)
    new_position = (position[0] + direction[0], position[1] + direction[1])

    if new_position[1] < 0 or new_position[0] < 0 or new_position[0] >= rows or new_position[1] >= cols:
        continue

    adjacent_elem = grid[new_position]
    
    if adjacent_elem in ['/', '\\']:
        new_direction = handle_mirror(direction, adjacent_elem)
    elif adjacent_elem in ['-', '|']:
        new_direction = handle_breaker(position, new_position, adjacent_elem, direction)
    else:
        new_direction = [direction]

    for nx, ny in new_direction:
        dx, dy = position[0] + nx, position[1] + ny
        if 0 <= dx < rows and 0 <= dy < cols and [new_position, (nx, ny)] not in seen:
            q.append([new_position, (nx, ny)])
            seen.append([new_position, (nx, ny)])

grid = [['.' for j in range(cols)] for i in range(rows)]
count = []
for elem in seen:
    grid[elem[0][0]][elem[0][1]] = '#'
    if elem[0] not in count:
        count.append(elem[0])

print(len(count))
# for x in grid:
#     print(x)