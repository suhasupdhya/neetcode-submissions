class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         suhas=set()
         for i in nums:
            if i in suhas:
                return True
            else:
                suhas.add(i)
         return False           