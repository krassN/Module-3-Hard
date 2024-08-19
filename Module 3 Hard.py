data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, int):
        s = data_structure
    elif isinstance(data_structure, str):
        s = len(data_structure)
    elif isinstance(data_structure, list) or isinstance(data_structure, set) or isinstance(data_structure, tuple):
        for element in data_structure:
            s += calculate_structure_sum(element)
    elif isinstance(data_structure, dict):
        keys, values = zip(*data_structure.items())
        s += calculate_structure_sum(keys)
        s += calculate_structure_sum(values)
    return s


result = calculate_structure_sum(data_structure)
print(result)
