def checkAccess(str):
    if str in dictionary[operation[1]]:
        print('OK')
    else:
        print('Access denied')
dictionary = {}
for _ in range(int(input())):
    lst = input().split()
    dictionary[lst[0]] = lst[1:]
operations = []
for _ in range(int(input())):
    operations.append(input().split())
for operation in operations:
    if operation[0] == 'write':
        checkAccess('W')
    elif operation[0] ==  'read':
        checkAccess('R')    
    elif operation[0] ==  'execute':
        checkAccess('X')
