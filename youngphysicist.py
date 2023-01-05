n = int(input())
sum = [0,0,0]
for i in range(n):
    input_ = input().split()
    sum[0] += int(input_[0])
    sum[1] += int(input_[1])
    sum[2] += int(input_[2])
if sum.count(0)==3:
    print("YES")
else :
    print("NO")
