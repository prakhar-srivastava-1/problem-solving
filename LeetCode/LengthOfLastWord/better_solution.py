class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip()
        for index, char in enumerate(s[::-1]):
            if char == ' ':
                break
            length += 1

        return length