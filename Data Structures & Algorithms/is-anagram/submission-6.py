class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        list_T = list(t)
        for char in s:
            if char in list_T:
                list_T.remove(char)
        
        if (list_T == []):
            return True
        else:
            return False