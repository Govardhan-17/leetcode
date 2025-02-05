class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string in the list as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Reduce the prefix until it matches the beginning of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # No common prefix found
        
        return prefix

# Test cases
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
