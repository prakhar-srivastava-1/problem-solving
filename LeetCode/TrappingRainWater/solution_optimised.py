
class Solution:
    def trap(self, height) -> int:
        """
            gets the total trapped water

            args:
                height (list): list containing height of each wall
            
            returns:
                total_water (int): total water accumulated
        """
        total_water = 0
        l = len(height)

        # corner cases
        # input length is 0 or 1 OR all heights are equal
        if l in (0, 1) or len(set(height)) == 1:
            return total_water

        # to track the max element seen so far at each index
        lmax, rmax = 0, 0

        # lists to hold left and right max values
        left = [0] * l
        right = [0] * l
        
        # move pointer from left to right
        # accumulates all max values 
        for i in range(l):
            if lmax < height[i]:
                lmax = height[i]
            left[i] = lmax
        
        # move pointer from right to left
        # accumulate all max values
        for i in range(l-1, -1, -1):
            if rmax < height[i]:
                rmax = height[i]
            right[i] = rmax 

        print(left)
        print(right)

        # accumulate trapped water
        for i in range(l):
            current_water = min(left[i], right[i]) - height[i]
            if current_water >= 1:
                total_water += current_water

        return total_water
        



sol = Solution()
print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))