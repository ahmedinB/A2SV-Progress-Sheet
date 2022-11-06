from collections import Counter
class Solution:
    def contains(self,mycounter , counter):
        found = False
        for mc,c in mycounter,counter :
            if mc[1] == c[1]:
                found = False



    def minWindowSubString(self, str, substr):
        c = Counter(substr)
        mycounter = c
        start, end = 0,0
        found = False
        minWindow = len(str)
        currentSubString = []
        while end < len(str):
            currentSubString.append(str[end])
#             check if the counters are
            if str[end] in substr:
                mycounter[str[end]] += 1
            while found and (start not in substr or mycounter[str[start]] > 1):
                start += 1
            min
            if
            end += 1




S = Solution()
print(S.minWindowSubString("ADOBECODEBANC", "ABC"))