class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        ans=[]
        for i in count.most_common(k):
            ai=i[0]
            ans.append(ai)

        return ans    


                           