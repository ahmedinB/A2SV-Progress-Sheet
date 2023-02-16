class Solution:
    def replaceElements(self, arr):
        i = len(arr) - 1
        ge = -1
        while i > -1:
            temp = arr[i]
            arr[i] = ge
            ge = max(temp, ge)
            i -= 1
        return arr

print(Solution().replaceElements([17,18,5,4,6,1]))
# [18,6,6,6,1,-1]
print(Solution().replaceElements([400]))