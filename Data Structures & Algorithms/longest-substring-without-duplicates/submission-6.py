class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=[]
        left=0
        ans=0
        for i in s:
            while i in seen:
                seen.remove (s[left])
                left+=1

            seen.append(i)  
            ans=max(ans,len(seen))
        return ans    
        