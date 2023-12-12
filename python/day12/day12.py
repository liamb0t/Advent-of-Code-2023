def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day12/data.txt'
data = [tuple(line.split()) for line in read_data_from_file(file_path)]

for seq, nums in [data[1]]:
    combinations = []
    queue = [int(n) for n in nums.split(',')]
    while queue:
        num = queue.pop(0)
        arrangement = '.' + ''.join(['#' for _ in range(num)]) + '.'
      
        for i, char in enumerate(seq):
            if char == '?':
                possible = True
                for s, a in zip(seq[num-i:i+num+1], arrangement):
                    print(seq[num-i:i+num+1], num, i, queue)
                    print(arrangement)
                    print(s, a)
                    print('\n') 
                    if s == '?' and a == '.':
                        pass
                    if s == '.' and a == '.':
                        pass
                    if s == '#' and a == '#':
                        pass
                    if s == '.' and a == '#':
                        possible = False
                    if s == '#' and a == '.':
                        possible = False
                if possible and i not in combinations:
                    combinations.append(i)

print(combinations)