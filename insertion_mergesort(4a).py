def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)

    for i in range(0,n1):
        L[i]=arr[l+i]
    for j in range(0,n2):
        R[j]=arr[m+1+j]

    i=0
    j=0
    k=l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1

def insertion_sort(alist):
    for i in range(1,len(alist)):
        temp=alist[i]
        j=i-1

        while(j>=0 and temp<alist[j]):
            alist[j+1]=alist[j]
            j=j-1
        alist[j+1]=temp

alist=input('Enter the insertion list of number:').split()
alist=[int(x) for x in alist]

insertion_sort(alist)
print('Sorted List:',end=' ')
print(alist)

def merge_sort(arr,l,r):
    if l<r:
        m=l+(r-l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

arr=input('Enter the merge list of numbers:').split()
arr=[int(x) for x in arr]
n=len(arr)

merge_sort(arr,0,n-1)
print("\n\nSorted Array is:")
for i in range(n):
    print("%d"%arr[i],end=" ")