#Quick sort
def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)

        return a
def quick(a,f,l):
    if f<l:
        pivot=f
        i=f
        j=l
        while i<j:
            while a[i]<=a[pivot] and i<l:
                i=i+1
            while a[j]>a[pivot]:
                j=j-1
            if i<j:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
        temp=a[pivot]
        a[pivot]=a[j]
        a[j]=temp
        quick(a,f,j-1)
        quick(a,j+1,l)
    return a

#input array
arr=input_num()
#call quick sort
first=0
last=len(arr)-1
sort_arr=quick(arr,first,last)
#print sorted array
print 'Sorted array:\n'
print sort_arr

