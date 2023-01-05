nums = list(map(int, input().split("+")))
resp = ""
for i in range(1,4):
    resp += (str(i)+"+")*nums.count(i)

print(resp[:-1])
    
    

