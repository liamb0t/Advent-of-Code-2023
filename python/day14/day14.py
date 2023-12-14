def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day14/data.txt'
data = [list(line) for line in read_data_from_file(file_path)]

round_rocks = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 'O']
total = 0

for rock in round_rocks:
    row, col = rock[0], rock[1]
    total += len(data) - row
    if row > 0:
        for i, upper_row in enumerate(data[:row][::-1], 1):
            if upper_row[col] == '.':
                total += 1
                data[row - i][col] = 'O'
                data[row - i + 1][col] =  '.'  
            else:
                break

print(total)