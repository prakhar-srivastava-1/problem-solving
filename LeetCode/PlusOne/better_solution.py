class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        c = 0
        digits = digits[::-1]
        
        for i in range(len(digits)):
            if digits[i] == 9:
                c = 1
                digits[i] = 0
            else: 
                digits[i] = digits[i] + 1
                return digits[::-1]
        
        if c == 1:
            return [1] + digits[::-1]