def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return [pattern.split('\n') for pattern in file.read().strip().split('\n\n')]

file_path = '2023/python/day13/data.txt'
patterns = read_data_from_file(file_path)

def horizontal_dist(pattern):
    rows = len(pattern)
   
    for i in range(1, rows):
        top_block = pattern[:i][::-1]
        bottom_block = pattern[i:]
        smudges = 0
        for r1, r2 in zip(top_block, bottom_block):
            for char1, char2 in zip(r1, r2):
                if char1 != char2:
                    smudges += 1
        if smudges == 0:
            return i
    return 0

def rotate(pattern):
    return ["".join(row) for row in zip(*pattern[::-1])]

print(sum([horizontal_dist(p) * 100 + horizontal_dist(rotate(p)) for p in patterns]))