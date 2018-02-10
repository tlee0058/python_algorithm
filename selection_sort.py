"""Selection Sort
If you're given a list with a bunch of numbers and you're supposed to sort the numbers (with the smallest number on the left and the largest number on the right), how would you do this? There are numerous sorting algorithms to sort numbers in the list. We'll introduce one of the simplest sorting algorithm called selection sort.

According to Wikipedia, selection sort"""

arr = [3,4,5,6,1,2]

for i in range(0, len(arr)-1):
    min = arr[0]  
    if arr[i] < min:
        arr[0], arr[i] = arr[i], arr[0]

for i in range(1, (len(arr))):
    min = arr[1]
    if arr[i] < min:
        arr[1], arr[i] = arr[i], arr[1]
        
for i in range(2, len(arr)):
    min = arr[2]
    if arr[i] < min:
        arr[2], arr[i] = arr[i], arr[2]

for i in range(3, (len(arr))):
    min = arr[3]
    if arr[i] < min:
        arr[3], arr[i] = arr[i], arr[3]

for i in range(len(arr)-1, len(arr)):
    min = arr[4]
    if arr[i] < min:
        arr[4], arr[i] = arr[i], arr[4]

print arr




