# In this program we try to find out the number wihich is greter than there consecutives number called as peakpoint
def findPeak(arr, n) :
    if(n==1):
        return 0
    if(arr[0]>= arr[1]):
        return 0
    if(arr[n-1]>=arr[n-2]):
        return 0
    a=[]
    for i in range(1, n-1):
        
        if ( arr[i]>= arr[i-1] and arr[i]>= arr[i+1]):
            a.append(i)
    return a 
         
arr = [10, 20, 15, 2, 23, 90, 67 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))


