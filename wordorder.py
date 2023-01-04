from collections import Counter
words = Counter([input() for _ in range(int(input()))])
print(len(words))
print(*words.values())
