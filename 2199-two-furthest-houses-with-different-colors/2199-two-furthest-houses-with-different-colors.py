class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        for i in range(len(colors)):
            for j in range(1,len(colors)):
                if colors[i]!=colors[j]:
                    k=abs(i-j)
                    ans=max(ans,k)
        return ans 