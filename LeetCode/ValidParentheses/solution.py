class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # corner cases
        # if length is odd
        if len(s) % 2 == 1: return False

        stack = []
        for index, char in enumerate(s):
            # append to stack
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
                # continue since we can only insert in this pass
                continue
            
            # pop from stack if you found a matching opening parentheses
            # should happen only when stack is not empty
            if len(stack) > 0:
                if stack[-1] == '{' and char == '}':
                    stack.pop()
                    
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                    
                elif stack[-1] == '(' and char == ')':
                    stack.pop()

                # if none of the conditions above matched => no matching pair
                else:
                    return False
            
            # if stack is empty => there is nothing to pop on seeing a closing bracket
            else:
                return False

        if len(stack) == 0:
            return True
        
        return False