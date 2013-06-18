Question 1:If you have a sorted array A and an unsorted array B,which is the best sorting algorithm among bubble,insertion and selection sort?

Answer:
Insertion sort
For insertion sort the best case is when the array is already sorted.Inserting an element to an already sorted list becomes easy.For a sorted list the inner for loop doesn't get executed at all.This means we can take one element at a time from the unsorted list and place it in the appropriate position in the sorted list.
No. of key comparisons=n-1
So time complexity=O(n)
Selection sort's best,worst and average time complexity is equal to O(n^2).So it doesnt matter if you sort the array or not
Bubble sort can be efficient if the array size is small.


Question 2:If you have a sorted array A and one more sorted array B,which is the best sorting algorithm among bubble,insertion and selection sort?

Answer:Selection sort works in the same way for both sorted and unsorted arrays.It's time complexity is O(n^2).We can use bubble sort if the sorted arrays are of small size.But the best sorting technique would be insertion sort.It's complexity is the same as in the previous question(since irrespective of whether the second array is sorted or not,we need to compare every element in the 2nd array with the elements in the 1st array and position it accordingly)


Question 3:If you are sorting the array by taking one value one after the other,which is a better sorting algorithm?

Answer:When we enter the elements one after the other individually,we make sure that it is placed in a sorted order by inserting it in the appropriate  position.
Both bubble sort and insertion sort can be used since the time complexity of sorting for both algorithms is O(n) in a sorted array.

=======
Sorting_algorithms
==================
>>>>>>> 09c3ede3f0015dbd8ea333826d910cc6ffafd3a3
