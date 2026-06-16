class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = {}
        for i in nums:
            if i not in hashed:
                hashed[i]=1
            else:
                hashed[i]+=1

        for v in hashed.values():
            if v>1:
                return True

        return False
        