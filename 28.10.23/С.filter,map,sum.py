print(sum(list(map(lambda x: x**2, list(filter(lambda x:x % 9 == 0, [element for element in range(10,100)]))))))
