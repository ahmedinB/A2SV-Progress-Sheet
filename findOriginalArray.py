class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort()
        mid= len(changed)//2
        l1=[]
        l2=[]
        zeros=0
        for i in changed:
            if i==0:
                zeros+=1
                changed.remove(0)
            elif i*2 in changed:

##              a problem with duplicated zeros how can you delete a duplicated item
                l1.append(i)
                l2.append(i*2)
                changed.remove(i*2)
        for z in range(0,zeros,2):
            l1.append(0)
            l2.append(0)
        if zeros%2!=0:
            return
        elif len(l1)!=mid or len(l1)==0:
            print("case", l1)
            return
        return changed

S=Solution()
print(S.findOriginalArray([0,0,0,0]))
