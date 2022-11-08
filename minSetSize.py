from collections import OrderedDict
class Solution(object):
    def counter(self, arr, dict):
        resp=[]
        for i in  dict:
            resp.append(arr.count(i))
        return resp

        # while
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict=list(OrderedDict.fromkeys(arr))
        half_size = len(arr) // 2
        counter=self.counter(arr, dict)
        print(counter)
        counter.sort(reverse=True)  
        ans = 0
        while half_size > 0:
            half_size -= counter[ans]
            ans += 1

        return ans
