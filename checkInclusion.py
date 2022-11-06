class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        i = 0
        j = len(s1)
        k = j-1

        found = False
        while i < len(s2)-j+1:
            while k >= 0:
                # if condition checking contains
                print (s2[i:i+j], s1[k], s2[i:i+j].__contains__(s1[k]))
                if s2[i:i+j].__contains__(s1[k]) and s1.count(s1[k])==s2[i:i+j].count(s1[k]):
                    found = True
                else :
                    found = False
                    break
                k-=1

            if found:
                return True
            i+=1
            k=j-1
        return False

S = Solution()
print (S.checkInclusion("hello", "ooolleooolleh"))