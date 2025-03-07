class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        
        ans=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    h=nums[j]-nums[i]
                    ans=max(h,ans)
                
        return ans
        