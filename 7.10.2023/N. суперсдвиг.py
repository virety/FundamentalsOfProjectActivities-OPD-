n = int(input())
a = list(map(int, input().split()))
k = int(input())
print(id(a))
if k > 0:
    k = k % n
    a = a[-k:] + a[:-k]
else:
    k = abs(k) % n
    a = a[k:] + a[:k]
print(id(a))
print(" ".join(str(x) for x in a))
