t = int(input())

for t_ in range(t):
    n = int(input())
    A = list(map(int, [*input().split()]))
    if sum(A) == 0:
        print("NO")
    else:
        print("YES")
        B = []
        for n_ in range (n-1, -1, -1):
            B.append(str(A[n_]))
        print(" ".join(B))