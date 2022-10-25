class Solution:
    def mySqrt(self, x: int) -> int:

        # handle basic cases - 0, 1
        if x in (0, 1): return x
        
        # will use binary search
        start = 1
        end = x
        mid = (start + end) // 2

        while mid * mid > x:
            sq_mid = mid * mid
            
            if sq_mid == x:
                return mid

            elif sq_mid > x:
                end = mid
            
            else:
                start = mid
            
            mid = (start + end) // 2

        # finally check the chunk where square of mid might exceed x
        while True:
            sq_mid = mid * mid
            if sq_mid == x:
                return mid
            
            if sq_mid > x:
                return mid - 1
            mid += 1