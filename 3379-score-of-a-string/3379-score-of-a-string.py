class Solution:
    def scoreOfString(self, n: str) -> int:
        l=len(n)
        count=0
        for i in range(l-1):
            k=abs(ord(n[i])-ord(n[i+1]))
            count+=k
            g=(count)
        
        return g
        