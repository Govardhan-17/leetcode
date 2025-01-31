class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1  # Store the sign
        x = abs(x)  # Work with the absolute value
        
        while x > 0:
            rev = rev * 10 + (x % 10)  # Append last digit
            x //= 10  # Remove last digit
        
        rev *= sign  # Restore the sign
        
        # Handle 32-bit integer overflow
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev

# Example usage
s1 = Solution()
print(s1.reverse(-123))  # Output: -321
print(s1.reverse(1534236469))  # Output: 0 (overflow case)
