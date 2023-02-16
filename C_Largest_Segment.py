n = int(input())
linesegments = []
lsmax_ = float('-inf')
lsmin_ = float('inf')
for i in range(n):
    ls = list(map(int, input().split()))
    linesegments.append(ls)
    lsmax_ = max(lsmax_, max(ls))
    lsmin_ = min(lsmin_, min(ls))

i = 1
found = False
for ls in linesegments:
    if ls[0] <= lsmin_ and ls[1] >= lsmax_:
        found = True
        break
    i+=1
if found:
    print(i)
else:
    print(-1)