class Solution:
    def lengthOfLongestSubString(self, str):
        maxlen = float ("-inf")
        set = []
        end = 0
        start = 0
        while end < len(str):
            set.append(str[end])
            while start < end and set.count(str[end]) > 1:
                # print (set)
                start += 1
                set.pop(0)
                maxlen = max(maxlen, len(set))
            # print(set)
            end += 1

        return maxlen

S = Solution()
print (S.lengthOfLongestSubString("PWWKEW"))