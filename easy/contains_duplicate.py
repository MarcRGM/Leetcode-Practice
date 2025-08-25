class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)

        return False
    
# instead of creating the set in one go, 
# we can return immediately if the element is in the set as we go through adding each one.