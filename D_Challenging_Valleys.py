t = int(input())
for t_ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    j = n //2
    ans = "YES"
    while j < n-1:
        if nums[j]>nums[j+1]:
            ans = "NO"
            break

        j+=1
    if nums[0] > nums[n-1]:
        ans = "NO"
    print(ans)
