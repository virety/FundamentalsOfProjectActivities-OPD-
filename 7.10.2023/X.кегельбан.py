N, K = input().split()
N = int(N)
K = int(K)

kegli = []
for i in range(N):
    kegli.append("I")
for i in range(K):
    l, r = input().split()
    l = int(l)
    r = int(r)
    for j in range(l-1, r):
        kegli[j] = "."
for i in kegli:
    print(i, end="")
