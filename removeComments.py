class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        #join the different elements with /n
        s = "/n".join(source)
        #use sliding windows to find the comment
        i,j = 0,0
        resp = []
        while i < len(s):
            if s[i:i+2]=="//" or s[i:i+2]=="/*":
                ## another loop to find where the comment ends
                while j < len(s):
                    if s[j+i:j+i+2]=="/n" or s[j+i:j+i+2]=="*/":
                        ## remove the comment
                        i=i+j
                        break
                    j+=1
            else:
                resp.append(s[i])
            i+=1
        #split the string with /n


        
        return resp
S = Solution()
print(S.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
##print(S.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
##                           i=-0
##                                           j=15  
####
