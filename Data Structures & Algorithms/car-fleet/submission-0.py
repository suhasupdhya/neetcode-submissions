class Solution:
    def carFleet(self, target: int, pos: List[int], sp: List[int]) -> int:
        car=zip(pos,sp)
        f=0
        fo=0
        cars=sorted(car,reverse=True)
        for pos,sp in cars:
            s=(target-pos)/sp
            if s>f:
                fo+=1
                f=s
        return fo       

        