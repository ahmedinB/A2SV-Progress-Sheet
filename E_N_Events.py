n = int(input())
events = []
for i in range(n):
    events.append(list(map(int, input().split())))
answer=0
i, j = 0, 1
while i < len(events):
    while j < len(events):
        if i!=j and events[i][0] < events[j][0] and events[j][1] < events[i][1]:
            answer+=1
            events.pop(j)
            j-=1
        j+=1
    i+=1
    j=i+1
print(answer )