class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=1
        result=[1]*n
        for i in range(n):
            result[i]=pref
            pref*=nums[i]
        suf=1
        for i in range(n-1,-1,-1):
            result[i]*=suf
            suf*=nums[i]
        return result        
        