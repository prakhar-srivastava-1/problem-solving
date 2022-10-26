class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle length is less than haystack length
        if len(haystack) < len(needle): return -1

        # two pointer approach
        start = 0
        end = len(needle)

        while end <= len(haystack):
            if needle == haystack[start: end]:
                return start
            
            start += 1
            end += 1
        
        return -1