def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day14/data.txt'

platform = [list(line) for line in read_data_from_file(file_path)]

def move_rocks(platform):
    rocks = [(i, j) for i in range(len(platform)) for j in range(len(platform[0])) if platform[i][j] == 'O']
    total = 0
    for rock in rocks:
        row, col = rock[0], rock[1]
        total += len(platform) - row
        if row > 0:
            for i, upper_row in enumerate(platform[:row][::-1], 1):
                if upper_row[col] == '.':
                    total += 1
                    platform[row - i][col] = 'O'
                    platform[row - i + 1][col] =  '.'  
                else:
                    break
    return total, platform

def rotate(pattern):
    return [list("".join(row)) for row in zip(*pattern[::-1])]

def cycle(num_cycles, platform):
    for cycle in range(num_cycles):
        for rotation in range(4):
            load, platform = move_rocks(platform)
            print(load)
            platform = rotate(platform)
    return move_rocks(platform)

cycle(100, platform)

