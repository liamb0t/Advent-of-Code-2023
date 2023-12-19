import copy

file_path = '2023/python/day19/data.txt'

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

data = read_data_from_file(file_path)
parts =  data.split('\n\n')[1].splitlines()
workflows = {}

for workflow in data.split('\n\n')[0].splitlines():
    rules = []
    key = workflow.split('{')[0]
    rules_data = workflow.split('{')[1][:-1].split(',')
    for rule in rules_data:
        if '<' or '>' not in rule:
            rules.append((rule))
        else:
            operation = '<' if '<' in rule else '>'
            part_name, val = rule.split(operation)[0], rule.split(operation)[1]
            destination_workflow = rule.split(':')[-1]
            rules.append((part_name, operation, val, destination_workflow))
    workflows[key] = rules


print(workflows)