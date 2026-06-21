class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        a=0
        l=0
        r=len(num)-1
        while l<r:
            s = num[l]+num[r]
            if s==target:
                return [l+1,r+1]
            elif s>target:
                r-=1
            else:
                l+=1        
        