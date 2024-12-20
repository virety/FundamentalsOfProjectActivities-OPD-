from sys import stdin

def codeSymbols(word):
    sum_codes = 0
    for symbol in word.upper():
        sum_codes += ord(symbol) - ord('A') + 1
    return sum_codes
words = [word for word in stdin.read().split()]
print(*[word for word in sorted(words, key=codeSymbols)], sep='\n')
