file_path = '2023/python/day21/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

data = read_data_from_file(file_path)
start = (0, 0)
rows = len(data)
cols = len(data[0])
rocks = [(i, j) for i in range(rows) for j in range(cols) if data[i][j] == '#']
start = [(i, j) for i in range(rows) for j in range(cols) if data[i][j] == 'S']
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def explore(plots, step, steps=64):
    if step == steps:
        return len(plots)

    new_plots = []

    for x, y in plots:
        for nx, ny in directions:
            dx = x + nx
            dy = y + ny
            if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in rocks and (dx, dy) not in new_plots:
                new_plots.append((dx, dy))
    return explore(new_plots, step + 1)

print(explore(start, 0))



        