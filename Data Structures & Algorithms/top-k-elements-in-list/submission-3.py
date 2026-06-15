class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        suhas=Counter(nums)
        for i in suhas.most_common(k):
            item=i[0]
            ans.append(item)
        return ans    



        