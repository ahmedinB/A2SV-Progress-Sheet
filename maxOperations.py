class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = dict()
        
        res = 0
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        for i in range(0, len(nums)):
            if hashmap[nums[i]] > 0:
                if (k - nums[i]) in hashmap and hashmap[k - nums[i]] > 0:
                    if (k - nums[i]) == nums[i]:
                        if hashmap[k - nums[i]] < 2:
                            continue
                    hashmap[nums[i]] -= 1
                    hashmap[k - nums[i]] -= 1
                    res += 1
        return res
