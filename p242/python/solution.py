class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        shift = ord("a")

        for c in bytes(s, "utf-8"):
            letters[c - shift] += 1

        for c in bytes(t, "utf-8"):
            letters[c - shift] -= 1

        for count in letters:
            if count != 0:
                return False

        return True
