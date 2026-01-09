class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}

        for s in strs:
            sorted_word = ''.join(sorted(s)) # sorted(s) returns a list
            # tuple(sorted((s)) for immutable key in dictionary
            if sorted_word in words:
                words[sorted_word].append(s) 
            else: 
                words[sorted_word] = [s]

            # shorter version
            # if sorted_word not in words:
                # words[sorted_word] = []
            # words[sorted_word].append(s)


            # Another solution using .setDefault() function without if else
            # words.setdefault(sorted_word, []).append(s)
            # setdefault(key, default) returns the value for key if it exists, 
            # otherwise it creates the key with default and returns that default value.

        return words.values()
    

# Neetcode's solution

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()