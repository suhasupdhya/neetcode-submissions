class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort=sorted(nums)
        
        s=len(nums)-k
        
        return sort[s]
        