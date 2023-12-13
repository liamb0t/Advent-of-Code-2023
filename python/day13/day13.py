def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return [pattern.split('\n') for pattern in file.read().strip().split('\n\n')]

file_path = '2023/python/day13/data.txt'
patterns = read_data_from_file(file_path)

def is_reflective_horizontal(pattern, pos='rows'):
    rows = len(pattern)
    is_even = rows % 2 == 0
    center = int(rows/2) if is_even else int((rows - 1)/2) + 1
    first_half = pattern[0 if is_even else 1:center]
    second_half = pattern[center:]  
 
    for x, y in zip(first_half[::-1], second_half):
        if x != y:
            return is_reflective_horizontal(rotate(pattern), 'cols')
    return center, pos

def rotate(pattern):
    rotated_pattern = ["".join(row) for row in zip(*pattern[::-1])]
    return rotated_pattern

rows = 0
cols = 0

for p in patterns:
    n, pos = is_reflective_horizontal(p)
    if pos == 'rows':
        rows += n
    else:
        cols += n

print(cols + rows*100)
