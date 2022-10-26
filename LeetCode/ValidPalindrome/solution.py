class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # clean in this pass
        s = s.lower()
        s_cleaned = ''

        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                s_cleaned = s_cleaned + char
        
        if s_cleaned == s_cleaned[::-1]:
            return True
        
        return False