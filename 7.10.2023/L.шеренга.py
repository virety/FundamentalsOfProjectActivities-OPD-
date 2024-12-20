N = int(input())
b = list(map(int, input().split()))
h = int(input())
k = 1
a=sorted(b, reverse=True)
for i in range(N):
    if a[i]>=h:
        k+=1
print(k)
