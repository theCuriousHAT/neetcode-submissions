class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p= sorted(t)
        q = sorted(s)

        if p==q:
            return True

        return False

        