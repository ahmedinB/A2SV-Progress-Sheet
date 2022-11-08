def countSwaps(a):
    swapCount=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                swapCount+=1
    print (f"""Array is sorted in {swapCount} swaps.  First Element: {a[0]} Last Element: {a[-1]}""")
