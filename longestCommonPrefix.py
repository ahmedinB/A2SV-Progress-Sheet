class Solution:
    def longestCommonPrefix(self, strs):
        commonprefix = strs[0]
        for str in strs:
            counter = 0
            if str == "":
                commonprefix = "" 
            for i in range(len(str)):
                if len(str)<len(commonprefix) and counter + 1 == len(str)\
                and commonprefix[i] == str[i]: 
                    commonprefix = str
                    break      
                if i>len(commonprefix)-1:
                    commonprefix = commonprefix[:counter]
                    break
                elif commonprefix[i] != str[i]:
                    commonprefix = commonprefix[:counter] 
                    break
                counter+=1

        return commonprefix


print(Solution().longestCommonPrefix(["abac","aba","aba"]))
