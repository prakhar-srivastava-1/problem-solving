class Solution:
    def is_palindrome(self, s):
        """
            checks if string is palindrome
            input: str
            returns: bool
        """
        return s == s[::-1]


    def longestPalindrome(self, s: str) -> str:
        
        len_s = len(s)

        # if length of string is 1 
        # OR there is only 1 distinct char 
        # OR the input string is palindrome
        if len_s == 1 or len(set(s)) == 1 or self.is_palindrome(s):
            return s

        # sentinel
        max_length = -999
        # result var
        max_palindrome = ""
        
        # start index
        i = 0
        
        while i < len_s:
            # take next char onwards
            j = i + 1
            while j <= len_s:
                if self.is_palindrome(s[i:j]) and j-i > max_length:
                    max_palindrome = s[i:j]
                    max_length = j-i
                j += 1
            
            i += 1

        return max_palindrome
