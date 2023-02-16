from collections import defaultdict
rep = int(input())
for i in range(rep):
    n = int(input())
    nums = [*input().split()]
    words = [*input()]
    d1 = defaultdict(list)
    index = 0
    while index < len(nums):
        d1[nums[index]].append(index)
        index+=1
    index = 0
    d2 = defaultdict(list)
    while index < len(words):
        d2[words[index]].append(index)
        index+=1
    index = 0
    answer = "YES"
    while index < len(words) and index < len(nums):
        if d1[nums[index]] != d2[words[index]]:
            for ch in d1[nums[index]]:
                if ch not in d2[words[index]]:
                    answer = "NO"
                    break
        index+=1
    print(answer)
