class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # operations=["x++","x--","++x","x++","++x"]
        X=0
        l=len(operations)
        for i in range(l):
            if operations[i]=="X++":
                X+=1
            if operations[i]=="X--":
                X-=1
            if operations[i]=="++X":
                X+=1
            if operations[i]=="--X":
                X-=1
        return X