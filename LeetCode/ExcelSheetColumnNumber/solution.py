class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # create dict of face values => O(26) ~ O(1)
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_dict = {char: index + 1 for index, char in enumerate(alpha)}

        # read the input string - as list
        columnTitle = list(columnTitle)[::-1]

        # column number 
        col = 0

        # O(n)
        for index, char in enumerate(columnTitle):
            # get value
            # = char_face_value * 26 ** index
            col += alpha_dict[char] * 26 ** index

        return col