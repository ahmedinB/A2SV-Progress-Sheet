class Solution:
    def isAlienSorted(self, words, order):
        n = len(order)
        map = {}
        for i in range(n):
            map[order[i]]=i
        prev = words[0]
        for word in words:
            for i in range(min(len(prev),len(word))):
                if map[prev[i]]>map[word[i]]:
                    return False
                elif map[prev[i]]<map[word[i]]:
                    break
                elif map[prev[i]]==map[word[i]] and len(prev) >len(word) and len(word) == i+1:
                    return False
            prev = word
        
        return True

S = Solution()
print(S.isAlienSorted(["zirqhpfscx","zrmvtxgelh","vokopzrtc",
                       "nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw",
                       "ttfwryy","dodpbbkp","akycwwcdog"],
                      "khjzlicrmunogwbpqdetasyfvx"))


print(S.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))
