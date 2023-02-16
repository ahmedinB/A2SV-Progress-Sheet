class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        resp = {}
        for l in cpdomains:
            l = l.split()
            c = int(l[0])
            domain = l[1]
            domain = domain.split(".")
            domain.reverse()
            for d in domain:
                print (d)
        return resp
####   response ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
S = Solution()
print(S.subdomainVisits(["9001 discuss.leetcode.com"]))
print(S.subdomainVisits(["9001 post.leetcode.com"]))
print(S.subdomainVisits(["9001 discuss.leetcode.com"]))

#  discuss   leetcode   com
#   discuss.leetcode.com  leetcode.com   com
