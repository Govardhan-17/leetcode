class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)//2
        k={}
        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        for j in k:
            if k[j]>l:
                return(j)
    
        