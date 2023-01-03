import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r'[^\w\s]', '', s)
        i, j = 0, len(s)-1
        print(s)
        while i <= j:
            if s[i]!= s[j]:
                return False
            i+=1
            j-=1
        return True

        
        
S = Solution()
print(S.isPalindrome("race a car"))
print(S.isPalindrome("A man, a plan, a canal: Panama"))
print('   spacious   '.replace("",""))