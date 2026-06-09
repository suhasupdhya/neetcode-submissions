class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gg=set()
        for i in nums:
          if i in gg:
            return True
          else:
              gg.add(i)
        return False