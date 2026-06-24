class Solution:
    def isValid(self, s: str) -> bool:
        suhas=[]
        dic={')':'(','}':'{',']':'['}
        for i in s:
            if i in dic:
                if not suhas or suhas.pop()!=dic[i]:
                    return False

            else:
                suhas.append(i)
        return not suhas            