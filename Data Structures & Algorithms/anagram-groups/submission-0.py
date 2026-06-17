class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed={}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashed:
                hashed[sorted_word]=[]

            hashed[sorted_word].append(word)

        return list(hashed.values())




        