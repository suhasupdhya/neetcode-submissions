class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        count=Counter(nums)
        for item in count.items():
            if item[1]>len(nums)//3:
                ans.append(item[0])
        return ans        
        
        