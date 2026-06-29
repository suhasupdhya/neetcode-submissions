class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp=""
        for ch in s:
            if ch.isalnum():
                sp+=ch.lower()
        
        if sp==sp[::-1]:
            return True
        else:
            return False    
        