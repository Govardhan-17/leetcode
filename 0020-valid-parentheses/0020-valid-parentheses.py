class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to match closing brackets with opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                if stack and stack[-1] == mapping[char]:  # If top of stack matches the corresponding opening bracket
                    stack.pop()  # Pop the top of the stack
                else:
                    return False  # If no match, return False
        
        # If the stack is empty, all brackets were matched; otherwise, return False
        return not stack

# Test cases
sol = Solution()
print(sol.isValid("()"))  # Output: True
print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("(]"))  # Output: False
print(sol.isValid("([])"))  # Output: True
