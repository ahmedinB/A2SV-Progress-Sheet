from collections import Counter
class Solution:
    def similarPairs(self, words):
        resp = 0
        # use two while loops 
        # chech the similarity (elements of i are in j)
        # 0 if nothing is similar
        i, j = 0, 1
        while i < len(words):
            similarChar = 0
            while j < len(words):
                similar = False
                word0 = [*words[i]]
                word1 = [*words[j]]
                word0.sort()
                word1.sort()
                word0 = list(set(word0))
                word1 = list(set(word1))
                # another loop to chech if the characters are similar
                if len(word0) == len(word1):
                    index = 0
                    similar = True
                    while index < len(word0):
                        if word0[index] != word1[index]:
                            similar = False
                        index+=1
                if similar:
                    similarChar+=1
                j+=1
            i+=1
            j=i+1
            resp += similarChar
        return resp
            
S = Solution()
print(S.similarPairs(["aba","aabb","abcd","bac","aabc"]))
print(S.similarPairs(["aabb","ab","ba"]))
print(S.similarPairs(["nba","cba","dba"]))
print(S.similarPairs(["dcedceadceceaeddcedc","dddcebcedcdbaeaaaeab","eecbeddbddeadcbbbdbb","decbcbebbddceacdeadd","ccbddbaedcadedbcaaae","dddcaadaceaedcdceedd","bbeddbcbbccddcaceeea","bdabacbbdadabbbddaea"]))
