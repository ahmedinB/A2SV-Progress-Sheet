class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        order = 1
        resp = ""
        # to alternate the order i am using odd and even numbers 
        while i < len(word1) and j < len(word2):
            if order%2==1:
                resp+=word1[i]
                i+=1
            else :
                resp+=word2[j]
                j+=1
            order+=1
        resp += word2[j:]
        resp += word1[i:]

        return resp
