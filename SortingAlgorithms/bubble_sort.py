# Bubble sort 

from typing import List

'''
In each iteration of this sorting algorithm, we compare adjacent numbers and swap them if they are in the wrong
order. Eventually, large numbers "bubble" to the end (or beginning) of the array). 

Things to note:
- the inner array has a range of 0 to len(arr) - 1 - i
  - we don't iterate to the last element because we will be comparing arr[j] with arr[j + 1]; iterating to the
    last element would cause an index out of bounds error
  - we also subtract i because the numbers at those indices are already sorted
- the implemention below will produce an array in ascending order; to get descending order, simply change > to <

Time complexity: O(n^2) because there are 2 loops
Space complexity: O(1) constant because we are sorting in place, no additional space required
'''
def bubbleSort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    return arr


numbers1 = [64, 34, 25, 12, 22, 11, 90]
numbers2 = [-2, 45, 0, 11, -9]
numbers3 = [1, 2, 3, 4, 5]
numbers4 = [1, 2, 3, 5, 4]

print(bubbleSort(numbers1))
print(bubbleSort(numbers2))
print(bubbleSort(numbers3))
print(bubbleSort(numbers4))

'''
Optimized version of bubble sort: since bubble sort will always make comparisons, even when
the array is already sorted, we can introduce a boolean variable to terminate the loop and
return the array early. 

Same time and space complexities.
'''
def optimizedBubbleSort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True
        
        if not swapped:
            return arr

    return arr

num1 = [64, 34, 25, 12, 22, 11, 90]
num2 = [-2, 45, 0, 11, -9]
num3 = [1, 2, 3, 4, 5]
num4 = [1, 2, 3, 5, 4]

print(optimizedBubbleSort(num1))
print(optimizedBubbleSort(num2))
print(optimizedBubbleSort(num3))
print(optimizedBubbleSort(num4))
