class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        h=""
        l=len(address)
        for i in range(l):
            if address[i]==".":
                  h+="[.]"
            else:
                h+=address[i]
        return(h)

        