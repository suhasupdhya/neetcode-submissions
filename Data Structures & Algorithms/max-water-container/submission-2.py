class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        l=0
        r=n-1
        maxi=0
        while l<r:
            a=min(h[l],h[r])*(r-l)
            maxi=max(maxi,a)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return maxi            


        