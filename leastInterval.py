class Solution(object):
    def findIDLE(self, tasks):
        k = 0
        i = 0
        idle = 0
        prefixsum = []
        while i < len(tasks):
            prefixsum.append(tasks[i])
            while k < i and tasks[:i].__contains__(tasks[i]):
                k += 1
            if k ==0:
                i += 1
        return idle
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        tasks.sort()
        i = 0
        j = len(tasks)-1
        resp = []

        while i!=j and i<j:
            # print(i,j)
            resp.append(tasks[i])
            resp.append(tasks[j])
            i+=1
            j-=1
        # self.findIDLE(list(map(lambda x : ord(x),resp)))
        self.findIDLE("".join(resp))
        # print (resp)
        return resp
S = Solution()
print (S.leastInterval(["A","A","A","B","B","B"],2))