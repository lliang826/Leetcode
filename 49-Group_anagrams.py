'''
49. Group anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
'''

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: value
        # # of letter occurences: [str]
        
        
        dict = defaultdict(list)

        for str in strs:
            chars = [0] * 26

            for char in str:
                chars[ord(char) - ord('a')] =+ 1

            dict[tuple(chars)].append(str)

        return dict.values()
    
