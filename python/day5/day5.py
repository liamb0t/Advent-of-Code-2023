def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day5/data.txt'
data = read_data_from_file(file_path)

seeds = [int(s) for s in data[0].split(':')[1].split()]
outputs = {i: False for i in range(len(seeds))}

for line in data[2:]:
    if line == '':
        outputs = {i: False for i in range(len(seeds))} 
   
    for i, seed in enumerate(seeds):
        if line != '':
            if line[0].isnumeric():
                map = [int(l) for l in line.split()]
                d, s, r = map[0], map[1], map[2]
                if s <= seed < s + r and outputs[i] == False:
                    output = d + (seed - s)
                    seeds[i] = output
                    outputs[i] = True

print(f'Part 1: {min(seeds)}')