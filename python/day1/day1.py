def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


file_path = '2023/python/day1/data.txt'
data = read_data_from_file(file_path)

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def string_is_num(string, num):
    if string == num:
        return True

def calibrate(data):
    sum = 0
    for line in data:
        first_digit = None
        second_digit = None
        for i in range(len(line)):
            if line[i].isnumeric():
                if not first_digit:
                    first_digit = int(line[i])
                second_digit = int(line[i])
            else:
                for num in numbers.keys():
                    if num in line:
                        if string_is_num(line[i:i+len(num)], num):
                            second_digit = numbers[num]
                            if not first_digit:
                                first_digit = numbers[num]
                        
        calibration_num = (first_digit * 10) + second_digit
        sum += calibration_num
    return sum

print(calibrate(data))