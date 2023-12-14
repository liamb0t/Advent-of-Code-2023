def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day14/data.txt'

platform = [list(line) for line in read_data_from_file(file_path)]

def tilt(platform):
    rocks = [(i, j) for i in range(len(platform)) for j in range(len(platform[0])) if platform[i][j] == 'O']

    for rock in rocks:
        row, col = rock[0], rock[1]
        if row > 0:
            for i, upper_row in enumerate(platform[:row][::-1], 1):
                if upper_row[col] == '.':
                    platform[row - i][col] = 'O'
                    platform[row - i + 1][col] =  '.'  
                else:
                    break
    return platform

def rotate(pattern):
    return [list("".join(row)) for row in zip(*pattern[::-1])]

def load(platform):
    return sum(row.count('O') * i for i, row in enumerate(platform[::-1], 1))

def cycle(num_cycles, platform):
    for cycle in range(num_cycles):
        for rotation in range(4):
            platform = tilt(platform)
            platform = rotate(platform)
        print(load(platform))

cycle(10000, platform)
