class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        suhas={}
        for i,a in enumerate(nums):
            diff=target-a
            if diff in suhas:
                return [suhas[diff],i]

            else:
                suhas[a]=i    

        