class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create roman_to_int dict
        char_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_dict = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500,
            'M': 1000,
        }
        s_reversed = s[::-1]

        """
                Char        Int Val         Index
                I             1             0
                V             5             1
                X             10            2
                L             50            3
                C             100           4
                D             500           5
                M             1000          6


                MCMXCIV
        
        M   C   M   X   C   I   V
        6   4   6   2   4   0   1
        M +(M - C) +(C-X) + (V-I)
    OR
        M - C + M - X + C - I + V
        1000
          + 900
                   + 90
                          + 4
        ===========================
                            1994
        ===========================
        V   I   C   X   M   C   M
        """
        int_number = roman_dict[s_reversed[0]]
        index = 0

        while index < len(s) - 1:
            curr_char, next_char = s_reversed[index], s_reversed[index+1]
            diff = char_list.index(curr_char) - char_list.index(next_char)
            if diff > 0:
                int_number -= roman_dict[next_char]
            else:
                int_number += roman_dict[next_char]
            
            index += 1
            
        return int_number
            