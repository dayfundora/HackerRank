def maximizeFinalElement(arr,n):
    arr.sort()
    if arr[0] != 1:
        arr[0]=1
    result=[arr[i-1]+1 if (arr[i]-arr[i-1]>1) else arr[i] for i in range(1, n)]
    return result[n-2]


n=4
arr=[3,1,3,4]
print(maximizeFinalElement(arr,n))