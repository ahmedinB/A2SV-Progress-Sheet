class Solution(object):
    def philip(self, arr, k):
        i = 0
        while k > i:
            arr[k], arr[i] = arr[i], arr[k]
            k -= 1
            i += 1

    # [3, 2, 4, 1]    k
    # 3, 2, 4, 1    3
    # 4, 2, 3, 1    4
    # 1, 3, 2, 4    2
    # 3, 1, 2, 4    3
    # 2, 1, 3, 4    2
    # 2, 1, 3, 4
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        max_ = max(arr)
        max_index = arr.index(max_)
        j = len(arr) - 1
        ans = []
        while j > 0:
            if max_index == 0:
                self.philip(arr, j)
                ans.append(j+1)
                j -= 1
                max_ = max(arr[:j + 1])
                max_index = arr.index(max_)

            else:
                self.philip(arr, max_index)
                ans.append(max_index+1)
                max_ = max(arr[:j + 1])
                max_index = arr.index(max_)
        return ans


print(Solution().pancakeSort([3,2,4,1]))
