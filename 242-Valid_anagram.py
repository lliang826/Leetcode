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

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
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
    def isAnagram1(self, s: str, t: str) -> bool:
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
    Another solution is to use an array to compare the letters in the strings. Since we know that the characters in the strings are 
    lowercase letters, we can create an array with 26 zeroes; the index represents the letter (letter 'a' is 0, 'b' is 1, etc.).
    Like the solution above, we have to iterate through the first string and count the characters, then iterate through the second
    string and determine if the characters are the same. Any non-zero indices mean that there are character differences.

    Time: O(n), where n is the length of the longer string, or n is 26 because we have to go through the alphabet
    Space: O(n), where n is the length of the alphabet => 26
    '''
    def isAnagram2(self, s: str, t: str) -> bool:
        letters = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            letters[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            letters[index] -= 1

        for i in letters:
            if i != 0:
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