s, n = list(map(int, [*input().split()]))

dragonslist = []
answer = "YES"
for i in range(n):
    dragonslist.append(list(map(int, [*input().split()])))

dragonslist.sort()

for dragon in dragonslist:
    
    if s > dragon[0]:
        s+=dragon[1]
    else:
        answer = "NO"
            

print(answer)
    