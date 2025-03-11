class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        
        ans=-1
        low =nums[0]
        for i in range(1,len(nums)):
            if low<nums[i]:
                k=nums[i]-low
                ans=max(ans,k)
            low=min(low,nums[i])

        return ans
        