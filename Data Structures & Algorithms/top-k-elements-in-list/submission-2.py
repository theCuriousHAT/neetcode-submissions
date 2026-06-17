class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashed={}
        lista = []
        for num in nums:
            hashed[num] = 1 + hashed.get(num, 0)

        for key, value in hashed.items():
            lista.append([value, key])

        lista.sort()

        res = []

        while len(res)<k:
            res.append(lista.pop()[1])
        return res
        