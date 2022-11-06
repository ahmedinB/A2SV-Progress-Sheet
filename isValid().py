class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isOpen=[]
        for i in s:
            print (i,)
            if i in ["(","[","{"]:
                isOpen.append(i)
            elif i in [")","]","}"]:
                if len(isOpen)==0:
                    return False
                if i==")" and isOpen[-1]=="(" or i=="]" and isOpen[-1]=="[" or\
                     i=="}" and isOpen[-1]=="{":
                    isOpen.pop(-1)
                else :
                    
                    return False
            
        if len(isOpen)==0:
            return True
        else:
            return False
S=Solution()
print(S.isValid("{{"))
