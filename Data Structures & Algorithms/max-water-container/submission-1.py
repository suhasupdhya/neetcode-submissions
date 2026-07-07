class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        a=0
        l=0
        r=n-1
        while l<r:
            for i in range(n):
                minimum=min(h[l],h[r])*(r-l)
                a=max(a,minimum)
                if h[l]<h[r]:
                 l+=1
                else:
                 r-=1
        return a        

                

        
        