class Solution:
    def compress(self, chars) -> int:

        len_chars = len(chars)

        # if there is only one char
        if len_chars == 1:
            return 1
        
        # if all distinct chars
        if len_chars == len(set(chars)):
            return len_chars

        start = 0 
        end = 1
        s = ""
        curr_char = chars[start]
        
        while end < len_chars:
            if curr_char == chars[end]:
                end += 1
            else:
                diff = end - start
                s = s + f"{curr_char}{diff}" if diff > 1 else s + f"{curr_char}"
                start = end
                end = start + 1
                curr_char = chars[start]
        
        diff = end - start
        s = s + f"{curr_char}{diff}" if diff > 1 else s + f"{curr_char}"
        chars[:] = list(s)
        return len(chars)