file_path = '2023/python/day19/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

data = read_data_from_file(file_path)
parts =  [[int(part.split('=')[1]) for part in line[1:-1].split(',')] for line in data.split('\n\n')[1].splitlines()]

workflows = {}

for workflow in data.split('\n\n')[0].splitlines():
    key = workflow.split('{')[0]
    rules_data = workflow.split('{')[1][:-1].split(',')
    rules = []
    for rule in rules_data:
        if '<' not in rule and '>' not in rule:
            rules.append((rule))
        else:
            operation = '<' if '<' in rule else '>'
            part_name, val = rule.split(operation)[0], int(rule.split(operation)[1].split(':')[0])
            destination_workflow = rule.split(':')[-1]
            rules.append((part_name, operation, val, destination_workflow))
        workflows[key] = rules


total = 0

for part in parts:
    current_workflow = 'in'
    processed = False
    x, m, a, s = part
    part_values = {'x': x, 'm': m, 'a': a, 's': s}
    while not processed:
        for rule in workflows[current_workflow]:
            try:
                part_name, operation, val, destination_workflow = rule

                if part_values[part_name] > val and operation == '>' or \
                    part_values[part_name] < val and operation == '<':

                    if destination_workflow in ['A', 'R']:
                        total += sum(part) if rule == 'A' else 0
                        processed = True
                    else:
                        current_workflow = destination_workflow
                        break

            except:
                if rule in ['A', 'R']:
                    total += sum(part) if rule == 'A' else 0
                    processed = True
                else:
                    current_workflow = rule
                    break

print(total)    