class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        # corner cases
        if len(height) in (0, 1):
            return 0

        # all heights are equal
        if len(set(height)) == 1:
            return 0

        for i, n in enumerate(height):
            # max in left subarray
            max_left = max(height[:i]) if height[:i] else -1
            # max in right subarray
            max_right = max(height[i+1:]) if height[i+1:] else -1
            
            chosen = min(max_left, max_right)
            current_water = chosen - n
            
            if current_water > 0:
                total_water += current_water
        
        return total_water
