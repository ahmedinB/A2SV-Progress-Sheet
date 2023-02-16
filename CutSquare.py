n = int(input())
for i in range(n):
    dim1 = list(map(int, [*input().split()]))
    dim2 = list(map(int, [*input().split()]))
    if min(dim1) + min(dim2) == max(dim1) and max(dim1) == max(dim2):
        print("YES")
    else:
        print("NO")
