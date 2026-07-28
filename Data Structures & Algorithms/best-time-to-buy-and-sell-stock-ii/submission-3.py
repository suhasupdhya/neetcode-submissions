class Solution:
    def maxProfit(self, p: List[int]) -> int:
        a=0
        for i in range(len(p)-1):
            if p[i]<p[i+1]:
                ai=p[i+1]-p[i]
                a+=ai
        return a        

                
        
        