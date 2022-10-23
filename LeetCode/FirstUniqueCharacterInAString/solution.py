class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a hash map to check if char is seen
        seen = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}

        for index, char in enumerate(s):
            # if char has not been seen
            if seen[char] == 0:
                # if char count is only one => return index
                if s.count(char) == 1:
                    return index
                # update seen to 1 for this char
                seen[char] = 1

        return -1