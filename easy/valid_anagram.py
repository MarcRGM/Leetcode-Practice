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
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if the letter is not on the dictionary, give it a value of 0 and add 1
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

# one liner answers: collections.Counter(s) == collections.Counter(t) AND sorted(s) == sorted(t)
# collections.Counter() is like a dictionary that counts how many times each element appears in a sequence