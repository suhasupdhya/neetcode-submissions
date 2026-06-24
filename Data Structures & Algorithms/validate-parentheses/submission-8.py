class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={']':'[','}':'{',')':'('}
        for i in s:
            if i in d:
                if not stack or stack.pop()!=d[i]:
                    return False
                    stack.append(i)
            else:
                stack.append(i)
        return not stack                
