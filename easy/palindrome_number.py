# Straightforward answer
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        orig = str(x)
        reverse = orig[::-1]
        return orig == reverse
        