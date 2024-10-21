'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a 
function to search target in nums. If target exists, then return its index. Otherwise, return -1.
'''

from typing import List


class Solution:
    '''
    Divide and conquer iterative solution. In each iteration, we are eliminating half of the possible outcomes
    to find the target. Low and high pointers are required (or left and right) to indicate the range, and a 
    middle pointer is required as well. 
    
    Since the input array is already sorted in ascending order, if the target is not found at the middle index, 
    we can eliminate either the lower half or the upper half depending on whether the target is less than or 
    greater than the value at the middle index.

    Time: O(log n), where n is the # of elements in the input array
        - In each iteration, we are dividing the array by 2 (n / 2 / 2 / 2 etc.)
        - Opposite of this would be n * 2 * 2 etc, which can be represented by exponents; exponents and logs
        are inverses of each other
    Space: O(1), constant memory
    '''
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # If we're dealing with large integers, adding low and high could introduce an integer overflow bug
            # mid = (low + high) // 2

            # Instead, find the difference between the two pointers and divide this value by 2; this gives us the
            # halfway point between the two pointers. Then, add this to the low pointer to get mid.
            mid = (high - low) // 2 + low
            
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
                
        return -1
    

solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))
print(solution.search([-1,0,3,5,9,12], 2))