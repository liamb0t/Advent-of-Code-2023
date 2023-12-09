def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day6/data.txt'
data = read_data_from_file(file_path)
    
times, records = [list(map(int, line.split(':')[1].split())) for line in data]

p2_time = int(''.join([str(x) for x in times]))
p2_record = int(''.join([str(x) for x in records]))

def is_record(charge, time):
    remaining = time - charge
    dist = remaining * charge
    if dist > record:
        return True

p1_answer = 1
p2_answer = 0
## part 1
for i in range(len(times)):
    ways = 0
    time, record = times[i], records[i]
    for c in range(1, time):
        if is_record(c, time):
            ways += 1
    p1_answer *= ways

## part 2
record = p2_record
for c in range(1, p2_time):
    if is_record(c, p2_time):
        p2_answer += 1

print(p1_answer)
print(p2_answer)
        

###chatGPT refactored solution of raw code

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

file_path = '2023/python/day6/data.txt'
data = read_data_from_file(file_path)

times = [int(t) for t in data[0].split(':')[1].split()]
records = [int(t) for t in data[1].split(':')[1].split()]
p2_time, p2_record = int(''.join(map(str, times))), int(''.join(map(str, records)))

def is_record(charge, time, record):
    remaining = time - charge
    return remaining * charge > record

# Part 1
p1_answer = 1
for time, record in zip(times, records):
    ways = sum(1 for c in range(1, time) if is_record(c, time, record))
    p1_answer *= ways

# Part 2
p2_answer = sum(1 for c in range(1, p2_time) if is_record(c, p2_time, p2_record))

print(p1_answer)
print(p2_answer)






