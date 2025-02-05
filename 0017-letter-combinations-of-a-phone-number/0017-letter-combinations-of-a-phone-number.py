class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        # Mapping digits to corresponding letters
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        # Backtracking function
        def backtrack(index, path):
            if index == len(digits):  # If the path length equals the digits length, add it to the result
                result.append(''.join(path))
                return
            
            current_digit = digits[index]
            for char in digit_to_char[current_digit]:
                path.append(char)
                backtrack(index + 1, path)  # Recurse with the next digit
                path.pop()  # Backtrack, remove the last character added
        
        backtrack(0, [])
        return result

# Test cases
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(""))  # Output: []
print(sol.letterCombinations("2"))  # Output: ["a","b","c"]
