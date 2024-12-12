def calculate(data):
    total_sum = 0

    if isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate(key)
            total_sum += calculate(value)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate(data_structure)
print(result)
