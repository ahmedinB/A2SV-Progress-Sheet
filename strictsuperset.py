# Enter your code here. Read input from STDIN. Print output to 
A = (input().split())
count = int(input())
N = []
for c in range(count):
    N.append((input().split()))
    
def strictsuperset(A, count, N):
    for row in N:
        for e in row:
            if e not in A:
                return False
            
    return True

print(strictsuperset(A,count,N))

# STDOUT
