# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
size = int(input())
roomNumbers = map(int, input().split())
roomNumbers = list(roomNumbers)

roomNumber = Counter(roomNumbers)
resp = [k for k, v in roomNumber.items() if v == 1]
print(resp[0])
