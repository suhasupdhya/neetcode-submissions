class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        ans=[]
        out=0
        for i in intervals:
            if not ans or ans[-1][1]<=i[0]:
                ans.append(i)
            else:
                out+=1
                if i[1] < ans[-1][1]:

                    ans[-1] = i
        return out            
        