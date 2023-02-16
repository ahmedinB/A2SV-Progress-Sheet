x=-121
reverse = 0
mod = x
while mod > 0:
    reverse = reverse*10 + mod%10
    mod = mod//10
    print (reverse,mod)
