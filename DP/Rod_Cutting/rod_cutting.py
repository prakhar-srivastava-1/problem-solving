# classic rod cutting problem from Cormen

profits = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
lengths = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# naive recursion
# cut from 1 to n - call on remaining length
def cut_rod(profits, n):
    # base case
    if n <= 1:
        return n

    # sentinel
    q = -999

    for i in range(1, n+1):
        q = max(q, profits[i] + cut_rod(profits, n-i))
        print(i, n-i, q)
    return q

print(profits)
print(lengths)
print(cut_rod(profits, 4))
print(cut_rod(profits, 5))
