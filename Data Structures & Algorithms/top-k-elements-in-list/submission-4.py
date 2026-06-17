class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        nums=Counter(nums)
        for i in nums.most_common(k):
            start=i[0]
            ans.append(start)
        return ans      