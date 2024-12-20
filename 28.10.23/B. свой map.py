def simple_map(function, values):
    result = []
    for value in values:
        result.append(function(value))
    return result

values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(simple_map(operation, values))
