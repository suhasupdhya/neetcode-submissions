from collections import Counter

class Solution:
    def removeDuplicates(self, nums):
        freq = Counter(nums)

        k = 0
        for num in freq:
            nums[k] = num
            k += 1

        return k