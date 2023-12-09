def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day9/data.txt'
data = read_data_from_file(file_path)

sequences = [list(map(int, (line.split()))) for line in data]

def f(seq):
    if all(element == 0 for element in seq[-1]):
        return seq
    else:
        last_seq= seq[-1]
        diffs = [last_seq[i + 1] - last_seq[i] for i in range(len(last_seq) - 1)]
        seq.append(diffs)
        return f(seq)

answers = []

for s in sequences:
    diffs = f([s])
    next_val = 0
    for i in range(len(diffs) - 1, -1, -1):
            next_val += diffs[i][-1]
    answers.append(next_val) 
   
print(sum(answers))
