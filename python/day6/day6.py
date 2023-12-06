from math import prod

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day6/data.txt'
data = read_data_from_file(file_path)

times = [int(t) for t in data[0].split(':')[1].split()]
dists = [int(t) for t in data[1].split(':')[1].split()]

p2_time = int(''.join([str(x) for x in times]))
p2_dist = int(''.join([str(x) for x in dists]))

answers = []

for i in range(len(times)):
    ways = 0
    time, record = times[i], dists[i]
    for charge in range(1, time):
        remaining = time - charge
        dist = remaining * charge
        if dist > record:
            ways += 1
    answers.append(ways)

print(prod(answers))

## part 2

p2_answer = 0
record = p2_dist
for charge in range(1, p2_time):
    remaining = p2_time - charge
    dist = remaining * charge
    if dist > record:
        p2_answer += 1

print(p2_answer)
        






