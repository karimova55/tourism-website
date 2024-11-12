def fibonacci(x,arr):
    n=len(arr)
    fm2=0
    fm1=1
    fm=fm2+fm1
    offset=-1
    while fm<n:
        fm2=fm1
        fm1=fm
        fm=fm2+fm1
    while fm>1:
        i=min(offset+fm2,n-1)
        if arr[i]<x:
            fm=fm1
            fm1=fm2
            fm2=fm-fm1
            offset=i
        elif arr[i]>x:
            fm=fm2
            fm1=fm1-fm2
            fm2=fm-fm1
        else:
            return i
    if fm1==1 and arr[offset+1]==x:
        return offset+1
arr=[1,5,7,8,9,12,15]
x=1
print(fibonacci(x,arr))

massivdan  sonni massivni fibanacci sonlari orqali indekslab massivni hamma elementiga murojaat qilmasdan qidiradi
