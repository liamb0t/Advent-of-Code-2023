def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(',')

file_path = '2023/python/day15/data.txt'

strings = read_data_from_file(file_path)

def hash(string):
    val = 0
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val

print(sum(hash(s) for s in strings))