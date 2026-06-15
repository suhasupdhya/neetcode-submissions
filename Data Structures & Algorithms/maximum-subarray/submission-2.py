class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total=0
        suhas=nums[0]
        for i in nums:
            if total<0:
                total=0

                
                
               

            
            total+=i
            suhas=max(total,suhas)
                
        return suhas        
            
