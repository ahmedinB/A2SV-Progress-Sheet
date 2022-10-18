##n,m,a=6,6,2

if m%a==0:
    m=m//a
elif m%a!=0:
    m=m//a+1
if n%a==0:
    n=n//a
elif n%a!=0:
    n=n//a+1
print(n*m)
