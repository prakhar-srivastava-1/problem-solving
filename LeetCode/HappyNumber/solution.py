class Solution:
    def sum_square_of_digits(self, n):
            total = 0
            while n != 0:
                d = n%10
                total += d * d
                n = n // 10
            return total
            
    def isHappy(self, n: int) -> bool:

        sq_sum = self.sum_square_of_digits(n)

        # capture the numbers seen
        seen = {}
        
        while sq_sum != 1:
            # repeat
            # if number already encountered => NOT a Happy Number
            if seen.get(sq_sum, False) == 1: return False
            # else add to hasmap
            else: seen[sq_sum] = 1
            
            # update the number to new number
            n = sq_sum
            # recalculate sum of squares for the next iteration
            sq_sum = self.sum_square_of_digits(n)

        # return True if loop is exited
        return True