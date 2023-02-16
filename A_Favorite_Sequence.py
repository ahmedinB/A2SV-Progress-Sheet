n = int(input())

for n_ in range(n):
    t = int(input())
    nums = list(map(int, input().split()))
    ans = []
    i, j = 0, t-1
    while i < j:
        ans.append(nums[i])
        ans.append(nums[j])
        i+=1
        j-=1
    if i == j and len(ans) < t:
        ans.append(nums[i])
    print(" ".join(map(str, ans)))
