def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

file_path = '2023/python/day12/data.txt'
universe = [[x for x in line] for line in read_data_from_file(file_path)]