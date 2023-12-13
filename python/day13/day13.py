def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return [pattern.split('\n') for pattern in file.read().strip().split('\n\n')]

file_path = '2023/python/day13/data.txt'
patterns = read_data_from_file(file_path)

def horizontal_dist(pattern):
    rows = len(pattern)
    for i in range(rows):
        symeterical = True
        for r1, r2 in zip(pattern[i::-1], pattern[i+1:]):
            if r1 != r2:
                symeterical = False
        if symeterical:
            return i + 1        
    return 0

def rotate(pattern):
    return ["".join(row) for row in zip(*pattern[::-1])]

print(sum(horizontal_dist(p) * 100 + horizontal_dist(rotate(p)) for p in patterns))