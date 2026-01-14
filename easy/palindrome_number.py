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
# Time complexity = O(n)
# Space complexity = O(n)

# Revert half of the number solution
# - Alexander Obregon
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        return x == reverted_number or x == reverted_number // 10