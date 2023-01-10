class Solution:
    def checknonzeroarea(self, a,b,c):
        if a+b > c and a+c > b and b+c > a:
            return True
        return False 
    def largestPerimeter(self, nums: List[int]) -> int:
        i = 2
        nums.sort()
        largestP = 0
        while i < len(nums):
            if not self.checknonzeroarea(nums[i-2],nums[i-1],nums[i]):
                i+=1
                continue        
            else:
                parameter = nums[i-2]+nums[i-1]+nums[i]
                print(parameter)
                largestP = max(largestP, parameter)
                i+=1
        return largestP
