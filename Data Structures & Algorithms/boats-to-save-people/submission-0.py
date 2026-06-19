class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        
        p=sorted(p)
        l=0
        r=len(p)-1
        boat=0
        while l<=r:
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
            boat+=1
            
        return boat            



        
        