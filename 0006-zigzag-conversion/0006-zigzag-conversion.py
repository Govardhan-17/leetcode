class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  # No change required

        rows = [""] * numRows  # List to store each row's characters
        index, step = 0, 1  # Initialize row index and direction

        for char in s:
            rows[index] += char  # Append character to current row

            # Change direction at top and bottom rows
            if index == 0:
                step = 1  # Move downward
            elif index == numRows - 1:
                step = -1  # Move upward

            index += step  # Move to the next row

        return "".join(rows)  # Join rows to get final result

# Example test cases
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(sol.convert("A", 1))  # Output: "A"
