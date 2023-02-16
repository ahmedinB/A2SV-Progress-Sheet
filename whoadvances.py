from collections import Counter, defaultdict
n, k = list(map(int, [*input().split()]))
scores = list(map(int, [*input().split()]))
answer = 0

ddict = set(scores)
count = []
for i in ddict:
    count.append([i,scores.count(i)])
count.sort(reverse=True)
for c in count:
    score = c[0]
    if score > 0:
        answer+=c[1]
    if answer >= k:
        break
print(answer)
