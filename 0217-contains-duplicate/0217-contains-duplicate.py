class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        d=set()
        f=False
        for i in nums:
            if i in d:
                f=True
                break
            d.add(i)
        if f==False:
            return False
        else:
            return True