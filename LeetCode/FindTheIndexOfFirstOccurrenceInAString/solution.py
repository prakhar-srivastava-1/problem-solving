class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle length is less than haystack length
        if len(haystack) < len(needle): return -1

        # return index of needle
        try:
            idx = haystack.index(needle)
        except:
            idx = -1 
        return idx