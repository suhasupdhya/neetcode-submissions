class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i]!=']':
                stack.append(s[i])
            else:
                strr=""
                while stack and stack[-1]!='[':
                    strr=stack.pop()+strr
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*strr)
        return "".join(stack)       

        