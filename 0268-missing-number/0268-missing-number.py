class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l+1):
            if i in nums:
                pass
            else:
                return i
        