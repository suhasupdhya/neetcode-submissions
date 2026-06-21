from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
    
        count=Counter(nums)
        for key in count:
            if count[key]>n//3:
                result.append(key)
        return result    
        
        