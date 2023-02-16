# ai≥ai−1 for all even i,
# ai≤ai−1 for all odd i>1.

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

i, j = 0, len(nums)-1
nums_ = []

for index_ in range(len(nums)):
    if index_%2 != 0:
        nums_.append(nums[j])
        j-=1
    else: 
        nums_.append(nums[i])
        i+=1
    
print(" ".join(map(str, nums_)))