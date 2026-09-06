class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s == t[::-1]) and (len(s) == len(t)):
            return True
        else:
            return False