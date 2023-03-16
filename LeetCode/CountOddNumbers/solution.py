class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # convert high and low from even to odd
        high = high - 1 if high % 2 == 0 else high
        low = low + 1 if low % 2 == 0 else low

        return (high - low) // 2 + 1