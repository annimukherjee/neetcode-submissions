class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_T = list(t)
        list_S = list(s)
        for char in list_S:
            if char in list_T:
                list_T.remove(char)
        
        if list_T == [] and len(s) == len(t):
            return True
        else:
            return False