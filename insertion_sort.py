def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)

        return a

def insert_sort(num):
    n=len(num)
    for i in range(n):
        for j in range(i,0,-1):
            if num[j-1]>num[j]:
                temp=num[j-1]
                num[j-1]=num[j]
                num[j]=temp
    return num

#input array elements
arr=input_num()
#call insertion sort
sort_arr=insert_sort(arr)
#print sorted array
print 'Sorted array is:\n'
print sort_arr
