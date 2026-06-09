class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return [list(i) for i in res]