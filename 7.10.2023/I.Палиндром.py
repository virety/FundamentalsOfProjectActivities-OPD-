N, K = map(int, input().split())
radio_parts = list(map(int, input().split()))

part_count = {}
count = 0 
for part in radio_parts:
    if part not in part_count: 
        if len(part_count) == K: 
            max_part = max(part_count, key=lambda x: part_count[x])
            part_count[max_part] -= 1  
            if part_count[max_part] == 0:  
                del part_count[max_part]

        part_count[part] = 1 
        count += 1

print(count)

