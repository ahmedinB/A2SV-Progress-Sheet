t = int(input())
cards = list(map(int, input().split()))
i, j = 0, t-1
first, second = 0, 0
while i < j:
    if cards[i] > cards[j]:
        first+= cards[i]
        i+=1
    elif cards[j] >= cards[i]:
        first+= cards[j]
        j-=1

    if cards[i] > cards[j]:
        second+= cards[i]
        i+=1
    elif cards[j] >= cards[i]:
        second+= cards[j]
        j-=1
if t%2 != 0:
    first+= cards[i]
print(first, second)