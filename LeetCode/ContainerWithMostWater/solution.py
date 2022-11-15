class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)

        # if only two elements are entered
        if len_height == 2 : return min(height)

        # init area
        max_area = 0
        # start and end pointers
        start = 0
        end = len_height - 1

        # keep looping until start and end cross
        while start < end:
            # get area
            area = min(height[start], height[end]) * (end - start)

            # if area > max_area => update
            max_area = area if area > max_area else max_area

            # shift from smaller side 
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return max_area