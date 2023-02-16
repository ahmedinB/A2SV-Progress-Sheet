n = int(input())
lengths = list(map(int, [*input().split()]))

def isTriangle(a, b, c):
    if a+b>c and a+c>b and c+b> a:
        return True
    return False

lengths.sort()

i = 0
answer = "NO"
while i < n-2:
    if isTriangle(lengths[i], lengths[i+1], lengths[i+2]):
        answer = "YES"
    i+=1

print(answer)