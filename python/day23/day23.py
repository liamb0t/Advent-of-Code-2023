file_path = 'advent/2023/python/day23/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

map = read_data_from_file(file_path)
rows = len(map)
cols = len(map[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(map)

q = [(0, 1, '.', 0)]
seen = set()
target = (22, 21)

while q:
    x, y, prev_slope, steps = q.pop(0)
    for nx, ny in directions:
        dx = x + nx
        dy = y + ny
        
        if not (0 <= dx < rows and 0 <= dy < cols):
            continue
        
        adjacent_tile = map[dx][dy]

        if adjacent_tile == '#':
            continue

        if (dx, dy) == target:
           print(steps + 1)

        if adjacent_tile == '>' and (nx, ny) == (0, 1) and prev_slope != adjacent_tile and (dx, dy) not in seen:
            seen.add((dx, dy))
            q.append((dx, dy, adjacent_tile, steps + 1))
       
        if adjacent_tile == '<' and (nx, ny) == (0, -1) and prev_slope != adjacent_tile and (dx, dy) not in seen:
            seen.add((dx, dy))
            q.append((dx, dy, adjacent_tile, steps + 1))
          
        if adjacent_tile == '.' and (dx, dy) not in seen:
            seen.add((dx, dy))
            q.append((dx, dy, prev_slope if nx != 1 else adjacent_tile, steps + 1))

        if adjacent_tile == 'v' and (dx, dy) not in seen:
            seen.add((dx, dy))
            q.append((dx, dy, adjacent_tile, steps + 1))