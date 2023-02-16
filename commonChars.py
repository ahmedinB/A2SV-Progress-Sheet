from collections import Counter
class Solution:
    def commonChars(self, words):
        word0 = [*words[0]]
        for word in words:
            index = 0
            while index < len(word0):
                if word0[index] not in word:
                    word0.remove(word0[index])
                    continue
                c0 = word0.count(word0[index])
                c = word.count(word0[index])
                w0 = word0[index]
                while c0 > c:
                    word0.remove(w0)
                    c0-=1
                    index-=1
                index+=1
        return word0

print(Solution().commonChars(["aabcdadb","cbabbbbd","bdbbcdaa","bccacaba","dddaabad","bdbddccc","bcdcdddb","dcbaccba"]))
print(Solution().commonChars(["daaccccd","adacbdda","abddbaba","bacbcbcb","bdaaaddc","cdadacba","bacbdcda","bacdaacd"]))