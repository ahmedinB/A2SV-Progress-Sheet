n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i, j = 0, 0
smaller = []
sm = 0
while j < m:
    while i < n and arr2[j] >  arr1[i]:
        sm+=1
        i+=1
    smaller.append(sm)
    j+=1

print(" ".join(map(str, smaller)))