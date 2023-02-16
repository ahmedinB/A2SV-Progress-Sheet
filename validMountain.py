class Solution:
    def validMountainArray(self, arr):
        i, j = 0, len(arr) - 1

        if len(arr) <= 2:
            return False

        while i+1 < j:
            if arr[i] == arr[i + 1] or arr[j] == arr[j - 1]:
                return False
            if arr[i] < arr[i + 1]:
                i += 1
            if arr[j] < arr[j - 1]:
                j -= 1
            if arr[i] > arr[i + 1] and arr[j] > arr[j - 1]:
                break
        if i+1 >= j and i != 0 and j != len(arr)-1:
            return True
        else:
            return False

print(Solution().validMountainArray([2,1]))
print(Solution().validMountainArray([1,3,2]))
print(Solution().validMountainArray([0,3,2,1]))
print(Solution().validMountainArray([0,2,3,4,5,2,1,0]))
print(Solution().validMountainArray([0,2,3,3,5,2,1,0]))
print(Solution().validMountainArray([2,0,2]))
print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))