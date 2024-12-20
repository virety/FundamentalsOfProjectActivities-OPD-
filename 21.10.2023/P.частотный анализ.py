from sys import stdin
from collections import Counter
words = stdin.read().split()
countWords = Counter(words) 
countWords = sorted(countWords.items(), key= lambda x:(-x[1],x[0]))
for words in countWords:
    print(words[0])
