class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # 32-bit integer max limit

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Subtract divisor using bit shifts (Optimized Division)
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return sign * quotient  # Apply sign to final result

# Example test cases
sol = Solution()
print(sol.divide(7, -3))   # Output: -2
print(sol.divide(10, 3))   # Output: 3
print(sol.divide(-10, -3)) # Output: 3
print(sol.divide(-2147483648, -1)) # Output: 2147483647 (handles overflow)
