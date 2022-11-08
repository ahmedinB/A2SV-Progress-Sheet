
class Solution: 
    def select(self, arr, i):
        # code here 
        min_i=i
        for counter in range(i+1,len(arr)):
            if arr[counter]<arr[min_i]:
                min_i=counter
        return min_i
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(n):
            selected=self.select(arr,i)
            arr[selected],arr[i]=arr[i],arr[selected]
    
        return arr
