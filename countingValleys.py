def countingValleys(steps, path):
    # Write your code here
    valleys=0
    pathSum=0
    prevSum=0
    for i in range(steps):
        if path[i]=="U":
            pathSum+=1
        elif path[i]=="D":
            pathSum-=1
        if pathSum<0 and prevSum>=0:
            valleys+=1
        prevSum=pathSum
    return valleys
print(countingValleys(10,"UDDDUDUUDU"))
