# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
# one liner answer: collections.Counter(s) == collections.Counter(t)
# collections.Counter() is like a dictionary that counts how many times each element appears in a sequence