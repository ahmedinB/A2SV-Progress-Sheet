n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i, j = 0, 0
merged = [0]*(n+m)
while i < n and j < m:
    if arr1[i] <= arr2[j]:
        merged[i+j]=arr1[i]
        i+=1 
    else:
        merged[i+j]=arr2[j]
        j+=1

while i < n:
    merged[i+j]=arr1[i]
    i+=1 
while j < m:
    merged[i+j]=arr2[j]
    j+=1 
print(" ".join(map(str, merged)))