from collections import defaultdict
class Solution:
    def findDuplicate(self, paths ):
        dupdict = defaultdict(list)
        for path in paths:
            path0 = path.split(" ")
            for p in path0[1:]:
#                 path0[0] is the directory
                p_ = p.split("(")
                dupdict [p_[1].strip(")")].append("".join(path0[0]) + "/" + "".join(p_[0]))
        answer = []
        for dup in dupdict.items():
            if len(dup[1]) > 1 :
                answer.append(dup[1])
        return answer
# [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))