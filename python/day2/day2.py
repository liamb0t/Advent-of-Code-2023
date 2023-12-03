from math import prod
import collections

file_path = '2023/python/day2/data.txt'

config = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_valid_game(data):
    game = data.split(':')[1].split(';')
    id = int(data.split(':')[0].split(' ')[1])
    for set in game:
        for cube in set.split(','):
            val = int(cube.split(' ')[1])
            color = cube.split(' ')[2]
            if val > config[color]:
                return None
    return id

###part 2

powers = []

def get_power(data):
    game = data.split(':')[1].split(';')
    maximums = collections.defaultdict(int)
    for set in game:
        for cube in set.split(','):
            val = int(cube.split(' ')[1])
            color = cube.split(' ')[2].strip()
            maximums[color] = max(maximums[color], val)
    return prod(maximums.values())

print(sum(map(get_power, open(file_path))))



