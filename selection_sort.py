#Selection sort
def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)

        return a
def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if nums[j]<nums[min]:
                min=j
        if min!=i:
            temp=nums[i]
            nums[i]=nums[min]
            nums[min]=temp

    return nums

#input the array
arr=input_num()
#call selection_sort
sort_arr=selection_sort(arr)
#print the sorted array
print 'The sorted array is:\n'
print sort_arr
            
