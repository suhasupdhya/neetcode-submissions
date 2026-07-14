class Solution:
    def numRescueBoats(self, p: List[int], t: int) -> int:
        n=len(p)
        p=sorted(p)
        l=0
        r=n-1
        o=0
        while l<=r:
                if p[l]+p[r]<=t:
                    l+=1
                r-=1
                o+=1
        return o           


              
        