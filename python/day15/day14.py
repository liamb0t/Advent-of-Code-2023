def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(',')

file_path = '2023/python/day15/data.txt'

init_seq = read_data_from_file(file_path)

def hash(string):
    val = 0
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val

def process_boxes(steps):
    boxes = {i: [] for i in range(256)}
    
    for step in steps:
        operation = '=' if '=' in step else '-'
        label = step.split(operation)[0]
        focal_length = int(step[-1]) if step[-1].isnumeric() else None
        box_num = hash(label)
        lens = (label, focal_length)
        existing_lens = [i for i, lens in enumerate(boxes[box_num]) if label == lens[0]]
        
        if operation == '=':
            if not existing_lens:
                boxes[box_num].append(lens)
            else:
                boxes[box_num][existing_lens[0]] = lens
        elif operation == '-' and existing_lens:
            boxes[box_num].pop(existing_lens[0])    

    return boxes

boxes = process_boxes(init_seq)
total = 0

for box_num, lenses in boxes.items():
    if any(lenses):
        for i, lens in enumerate(lenses, 1):
            focal_length = lens[1]
            total += (box_num + 1) * i * focal_length

print(total)