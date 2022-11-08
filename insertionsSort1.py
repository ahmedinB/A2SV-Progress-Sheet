def insertionSort1(n, arr):
    # Write your code here
    num=arr[-1]
    inserted=False
    for i in range(n-1,-1,-1):
        if not inserted:
            if i==0:
                arr[i]=num
            elif num < arr[i-1]:
                arr[i]= arr[i-1]
            elif num > arr[i-1]:
                arr[i]=num
                inserted=True
            printList(arr)
