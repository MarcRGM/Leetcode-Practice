class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}

        for s in strs:
            sorted_word = ''.join(sorted(s)) # sorted(s) returns a list
            if sorted_word in words:
                words[sorted_word].append(s) 
            else: 
                words[sorted_word] = [s]
        return words.values()