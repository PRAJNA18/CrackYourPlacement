class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(' : ')', '{' : '}', '[' : ']'}

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return not stack