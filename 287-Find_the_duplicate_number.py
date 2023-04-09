# DESCRIPTION
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


# Floyd's tortoise and hare algorithm
# Time: 
# Space: 



# Not the real solution, but if we had extra space then we could use a hashmap/dictionary
# Can also use a set
# Time: O(n)
# Space: O(n)
def findDuplicateNumber_hashMap(intArray):
    dict = {}
    for i in intArray:
        if i in dict:
            return i
        else:
            dict[i] = 1

test1 = [1,3,4,2,2]
test2 = [3,1,3,4,2]

print(f"test1: {findDuplicateNumber_hashMap(test1)}")
print(f"test2: {findDuplicateNumber_hashMap(test2)}")


# If we could modify the array then we could sort it in the first iteration, then
# look for adjacent repeating numbers in the second iteration 
# Time: O(n log n)
# Space: O(1)