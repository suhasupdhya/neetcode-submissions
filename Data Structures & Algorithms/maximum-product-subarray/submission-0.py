class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1

        for n in nums:
            temp = curMax * n

            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, temp, curMin * n)

            res = max(res, curMax)

        return res