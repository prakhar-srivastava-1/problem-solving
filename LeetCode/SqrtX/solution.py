class Solution:
    def mySqrt(self, x: int) -> int:
        
        # handle cases when input = 0 or 1
        if x in (0, 1): return x

        for i in range(1, x//2 + 2):
            sq = i * i 

            if sq == x:
                return i

            # as soon as sq goes beyond x => return i - 1
            if sq > x:
                return i - 1

            

