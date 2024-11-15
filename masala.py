def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        mid_val=arr[mid]
        if target==mid_val:
            return mid
        elif mid_val<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[4,5,6,7,8,11]
target=45
print(binary_search(arr,target))
