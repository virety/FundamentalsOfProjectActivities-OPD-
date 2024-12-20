from math import log
def check_pin(pin):
    pin = pin.split('-')
    if f(pin[0]) and pin[1] == pin[1][::-1] and log(int(pin[2]), 2) == int(log(int(pin[2]), 2)): return 'Корректен'
    return 'Некорректен'
def f(n):
    return all(int(n) % i != 0 for i in range(2, int(int(n)**0.5)+1))
print(check_pin("12-22-16"))
