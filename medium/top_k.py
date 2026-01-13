class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums: # See how many times each number appears
            count[n] = count.get(n, 0) + 1

        sorted_items = sorted(count.items(), key=lambda i: i[1], reverse=True)
        # get the items from count, look at the second value (key,value) which is the frequency, 
        # and reverse, which means, highest first

        return list(map(lambda x: x[0], sorted_items))[:k]
        # keep only the first value, throw away the frequency and take the first k numbers


# Neetcode solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # create buckets

        for n in nums: 
            count[n] = count.get(n, 0) + 1 # See how many times each number appears
        for n, c in count.items():
            freq[c].append(n)
        # Index = frequency
        # Value = list of numbers with that frequency

        res = []
        for i in range(len(freq) - 1, 0, -1): # (Start at length - 1, stop at 0, decrement by 1)
            for n in freq[i]: # start extracting nums with higher frequency first
                res.append(n)
                if len(res) == k: # stop when res collected k numbers
                    return res
