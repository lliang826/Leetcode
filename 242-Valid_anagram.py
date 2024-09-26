'''
242. Valid anagram

DESCRIPTION:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

'''
To check if the two strings are anagrams of one another, we have to use a hashmap (or in Python, a dictionary). We can't use a set
because a string can have repeating characters. We store the hashmap as "character: # of times character appears". First, we iterate
through string s and populate the hashmap. Then, we iterate through the string t: if a character does not exist in the hashmap, we 
can instantly return False (a character exists in t that does not exist in s); otherwise, we can decrement the character's counter 
in the hashmap. Finally, we iterate through the hashmap and check if any counters are not equal to 0. Positive counter numbers mean
that there is a character that exists in s that does not exist in t; negative counter numbers mean that a character exists in t that 
does not exist in s. 

Time: O(n) - must iterate through all the characters in both strings
Space: O(n) - storing all the characters of one string into a hashmap/dictionary
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = dict()

        for char in s:
            if char in charMap:
                charMap[char] += 1
            else: 
                charMap[char] = 1

        for char in t:
            if char not in charMap:
                return False
            else:
                charMap[char] -= 1

        for key in charMap:
            if charMap[key] != 0:
                return False

        return True
    

'''
Test cases:
s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

s = ""
t = ""
'''