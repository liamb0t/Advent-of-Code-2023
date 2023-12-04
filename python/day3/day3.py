from math import prod
import collections

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day3/data.txt'
data = read_data_from_file(file_path)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
rows = len(data)
cols = len(data[0])

answers = []
gears = collections.defaultdict(int)

for i in range(rows):
    num = ''
    possible = False
    gear_loc = None
    for j in range(cols):
        char = data[i][j]
        if char.isnumeric():
            num += char
            for dr, dc in directions:
                new_row, new_col = i + dr, j + dc 
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if not data[new_row][new_col].isnumeric() and data[new_row][new_col] != '.':
                        possible = True
                        if data[new_row][new_col] == '*':
                          gear_loc = (new_row, new_col)
                        
        if j == cols - 1 or not char.isnumeric():
            if possible:
                answers.append(num)
                if gear_loc:
                    if gears[gear_loc]:
                        gears[gear_loc] = [gears[gear_loc], int(num)]
                    else:
                        gears[gear_loc] = int(num)
            num = ''
            possible = False
            gear_loc = None

print(sum([prod(part) for part in gears.values() if type(part) == list]))
print(sum([int(a) for a in answers]))


