i = int(input())
for i_ in range(i):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    j = 0
    ans = "YES"
    while j < len(a)-1:
        if abs(a[j]-a[j+1]) > 1:
            ans = "NO"
            break
        j+=1
    print(ans)