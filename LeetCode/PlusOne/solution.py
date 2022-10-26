class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''

        for digit in digits:
            n = n + str(digit)

        n = str(int(n) + 1)

        return list(n)