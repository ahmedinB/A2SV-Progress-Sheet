class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        sortedS=""
        for i in range(0,s.__len__()):
            for j in range(0,s.__len__()):
                if s[j].__contains__(str(i+1)):
                    sortedS+=s[j][:s[j].__len__()-1] + " " 
        return sortedS[:sortedS.__len__()-1]
