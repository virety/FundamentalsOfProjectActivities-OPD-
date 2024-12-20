n, m = map(int, input().split())
a= []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
ab = []
for j in range(m):
    abc= []
    for i in range(n):
        abc.append(a[i][j])
    ab.append(abc)
for row in ab:
    print(*row)
