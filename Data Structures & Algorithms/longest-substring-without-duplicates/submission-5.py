class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = []
        ans=0
        

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.append(s[right])
            ans=max(ans,len(seen))
            

        return ans