class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l=len(jewels)
        k=len(stones)
        count=0
        for i in range(l):
        
            for j in range(k):
                if jewels[i]==stones[j]:
                    count+=1
        return count
