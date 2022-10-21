# classic rod cutting problem from Cormen
# starting with the recursive solution
class RodCutting(object):
    def __init__(self):
        self.profits = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.lengths = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # to memoize
        self.memo = dict()

    # naive recursion
    # cut from 1 to n - call on remaining length
    def cut_rod(self, n):
        # add cache check
        if n in self.memo:
            return self.memo[n]
        # base case
        if n <= 1:
            return n

        # sentinel
        q = -999

        for i in range(1, n+1):
            q = max(q, self.profits[i] + self.cut_rod(n-i))
            print(i, n-i, q)
        self.memo[n] = q
        return q

rod = RodCutting()
print(rod.profits)
print(rod.lengths)
print(rod.cut_rod(4))
print(rod.memo)
print(rod.cut_rod(5))
print(rod.memo)
print(rod.cut_rod(8))
print(rod.memo)
