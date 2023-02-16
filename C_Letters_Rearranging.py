t = int(input())
strs = []
from collections import Counter
def isPalindrome(str):
    i, j = 0, len(str)-1
    while i < j:
        if str[i]!=str[j] :
            return False
        i+=1
        j-=1
    return True

# append the string input in a list
for t_ in range(t):
    strs.append(input())
    

for str in strs:
    if not isPalindrome(str):
        print(str)
        continue
    counts = Counter(str) 
    maxcount = max(counts.values())   
    if len(str)==maxcount:
        print(-1)
        continue
    minchar = ""
    mincount = len(str)
    for count in counts.items():
        if count[1] < mincount:
            minchar = count[0]
            mincount = count[1]
    
    str = [*str] 
    index = str.index(minchar)
    if  index + 1 < len(str) and minchar != str[index+1]:
        str[index], str[index+1] = str[index+1], str[index]

    print("".join(str))
    