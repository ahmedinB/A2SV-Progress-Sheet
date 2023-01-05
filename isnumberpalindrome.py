class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverse = 0
        mod = x
        while mod > 0:
            reverse = reverse*10 + mod%10
            mod = mod//10
        if reverse == x:
            return True
        return False
