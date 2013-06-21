def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs\n'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)
        return a

def sort(a):
    n=len(a)
    b=[]
    width=1
    while width<n:
        i=0
        while(i<n):
            merge(a,i,min(i+width,n),min(i+2*width,n),b)
            i=i+2*width
        a[0:n]=b[0:n]
    width=2*width
    return a

def merge(a,l,r,e,b):
    i=l
    j=r

    for k in range(l,e):
        if i<r and (j>=e or a[i]<=a[j]):
            b.append(a[i])
            i=i+1
        else:
            b.append(a[j])
            j=j+1
    return b

def min(x,y):
        if x<y:
                return x
        else:
                return y

arr=input_num()
sort_arr=sort(arr)
print 'Sorted array\n'
print sort_arr
