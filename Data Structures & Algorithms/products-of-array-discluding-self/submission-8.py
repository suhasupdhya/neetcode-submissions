class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=1
        ans=[1]*n
        for i in range(n):
            ans[i]=pref
            pref=pref*nums[i]
            
        suf=1
        for i in range(n-1,-1,-1):
            ans[i]*=suf
            suf*=nums[i]
        return ans    

        