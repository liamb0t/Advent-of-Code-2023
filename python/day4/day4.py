from math import prod
import collections
import time

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day4/data.txt'
data = read_data_from_file(file_path)


points = 0

for line in data:
    score = 0
    win_nums = [int(x) for x in line.split(':')[1].split('|')[0].strip().split(' ') if x.isnumeric()]
    guesses = [int(x) for x in line.split(':')[1].split('|')[1].strip().split(' ') if x.isnumeric()]
    matches = 0
    for guess in guesses:
        if guess in win_nums:
            matches += 1
    if matches > 0:
        score =  1 * 2 ** (matches - 1)
    points += score

#print(points)

##part2 

counts = [1] * len(data)
cards = collections.defaultdict(int)

for i, line in enumerate(data):
    matches = 0
    win_nums = [int(x) for x in line.split(':')[1].split('|')[0].strip().split(' ') if x.isnumeric()]
    guesses = [int(x) for x in line.split(':')[1].split('|')[1].strip().split(' ') if x.isnumeric()]
    for guess in guesses:
        if guess in win_nums:
            matches += 1
    cards[i] = matches

for i in range(len(data)):
    for j in range(i + 1, i + cards[i] + 1):
        counts[j] += counts[i]
        print(f'Your {counts[i]} copies of card {i} have {cards[i]} matching numbers, so you win {counts[i]} copies of card {j}')
        time.sleep(0.2)
print(sum(counts))


    


