n = int(input())
for n_ in range(n):
    t = int(input())
    binary = input()
    i, j = 0, t-1
    while i < j:
        li = binary[i], binary[j]
        if "0" in li and "1" in li:
            # binary.pop(j)
            # binary.pop(i)
            i+=1
            j-=1
        else:
            break
    print(len(binary[i: j+1]))

