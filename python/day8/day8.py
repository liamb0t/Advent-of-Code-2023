def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day8/data.txt'
data = read_data_from_file(file_path)

instructions = data[0]

elems = {line.split('=')[0].strip(): tuple(line.split('=')[1].strip()[1:-1].split(', ')) for line in data[2:]}

# steps = 0
# key = 'AAA'

# while key != 'ZZZ':
#     for i in instructions:
#         index = {'R': 1, 'L': 0}[i]
#         key = elems[key][index]
#         steps += 1
#print(steps)

starting_index = {'R': 1, 'L': 0}[instructions[0]]

nodes = {node: '' for node, values in elems.items() if node.endswith('A')}
chars = {node: '' for node, value in nodes.items()}


steps = 0
terminate = False

while terminate == False:
    for i in instructions:
        index = {'R': 1, 'L': 0}[i]
        for node, val in nodes.items():
            if val:
                nodes[node] = elems[val][index]
            else:
                nodes[node] = elems[node][index]
            chars[node] = nodes[node][2]
        if len(set(chars.values())) == 1:
            print(chars, steps)
            if list(set(chars.values()))[0] == 'Z':
                terminate = True
        steps += 1
     

print(steps)
    
