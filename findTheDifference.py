from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s+t) 
        for i in count:
            if count[i]%2==1:
                return i
