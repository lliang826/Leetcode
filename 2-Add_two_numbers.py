'''
2. Add two numbers

DESCRIPTION:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse 
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
My own solution for this problem (definitely not the best). Instead of dealing with the carry overs and the 
modulus that would come with adding 2 numbers, I iterate through the linked lists and convert the values 
into integers before performing the addition. To do so, I convert each value to a string and concatenate them. 
Since the digits are stored in reverse order, I using slicing to reverse the strings before converting them 
to integers. The sum is finally returned as a new linked list.

Time: O(n) - we need to iterate through all the digits of l1, l2 and the sum (whichever is longest)
Space: O(n) - a new linked list is created for the sum
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstString = ""
        while l1:
            firstString += str(l1.val)
            l1 = l1.next

        secondString = ""
        while l2:
            secondString += str(l2.val)
            l2 = l2.next
        
        firstString = firstString[::-1]
        secondString = secondString[::-1]

        firstInt = int(firstString)
        secondInt = int(secondString)

        sum = firstInt + secondInt
        stringSum = str(sum)

        head = ListNode(0)
        curr = head
        for i in range(len(stringSum) - 1, -1, -1):
            node = ListNode(int(stringSum[i]))
            curr.next = node
            curr = curr.next

        return head.next
    
    
    def listToLinkedList(self, arrayList: List[int]):
        head = ListNode(0)
        curr = head
        for i in arrayList:
            node = ListNode(i)
            curr.next = node
            curr = curr.next

        return head.next
    

    
solution = Solution()

l1 = solution.listToLinkedList([2, 4, 3])
l2 = solution.listToLinkedList([5,6,4])
head = solution.addTwoNumbers(l1, l2)
array = []
while head:
    array.append(head.val)
    head = head.next
print(array)

l1 = solution.listToLinkedList([0])
l2 = solution.listToLinkedList([0])
head = solution.addTwoNumbers(l1, l2)
array = []
while head:
    array.append(head.val)
    head = head.next
print(array)

l1 = solution.listToLinkedList([9,9,9,9,9,9,9])
l2 = solution.listToLinkedList([9,9,9,9])
head = solution.addTwoNumbers(l1, l2)
array = []
while head:
    array.append(head.val)
    head = head.next
print(array)