class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}

        for i, num in enumerate(nums):
            complement = target-num

            if complement in hashed:
                return [hashed[complement], i]

            hashed[num]=i

        return []


        