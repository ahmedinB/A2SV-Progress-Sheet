def findMaxSum(nums,k):
    maxsum = float('-inf')
    i = 0
    currentSum = sum(nums[:k])
    while i < len(nums)-k:
        currentSum = currentSum + nums[i+k] - nums[i]
        maxsum = max(maxsum, currentSum)
        i += 1
    return maxsum
print (findMaxSum([4,2,1,7,8,1,2,8,1,0],3))