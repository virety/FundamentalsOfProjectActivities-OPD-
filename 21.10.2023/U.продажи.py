from sys import stdin
record = {}
for element in stdin.readlines():
    element = element.split()
    record.setdefault(element[0], {})
    if element[1] in record[element[0]]:
        record[element[0]][element[1]] += int(element[2])
        continue
    record[element[0]][element[1]] = int(element[2]) 
sorted_names = sorted(record.keys())
for name in sorted_names:
    print(name + ':')
    sorted_items = sorted(record[name].keys())
    for item in sorted_items:
        print(f"{item} {record[name][item]}")
