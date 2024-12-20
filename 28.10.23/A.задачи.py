N= int(input())
arr = []
for i in range(N):
    K = int(input())
    arr2 = []
    for j in range(K):
        M = input()
        arr2.append(M)
    arr.append(arr2)
all_passed = all(any(int(student.split()[1]) > 1 for student in group) for group in arr)
if all_passed:
    print("ДА")
else:
    print("НЕТ")
