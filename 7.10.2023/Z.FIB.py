n = int(input())
f1 = f2 = 1
if n==1:
    print("1")
if n==0:
    print(" ")
if n>=2:
    print(f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
