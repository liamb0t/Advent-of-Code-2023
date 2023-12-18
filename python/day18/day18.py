file_path = '2023/python/day18/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

plan = read_data_from_file(file_path)
trenches = []
directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
r, c = 0, 0

for line in plan:
    dir, moves, color = line.split()[0], int(line.split()[1]), line.split()[2]
    nr, nc = directions[dir]
  
    for i in range(moves + 1):
        trenches.append((r + i*nr, c) if nr != 0 else (r, c + i*nc))
        
    r += nr * moves
    c += nc * moves

print(trenches)

 

