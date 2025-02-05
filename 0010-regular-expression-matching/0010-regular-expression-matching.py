class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True  # Both strings are empty, they match
        
        # Handle patterns like a*, a*b*, a*b*c* matching an empty string s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # '*' can match zero occurrences of the previous char
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # If current chars match, carry the match from the previous state
                elif p[j - 1] == '*':
                    # '*' can match zero occurrence of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # '*' can match one or more occurrences of the preceding element
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[m][n]  # Return the result for the full string match

# Test cases
sol = Solution()
print(sol.isMatch("aa", "a*"))  # Output: True
print(sol.isMatch("aa", "a"))   # Output: False
print(sol.isMatch("ab", ".*"))  # Output: True
