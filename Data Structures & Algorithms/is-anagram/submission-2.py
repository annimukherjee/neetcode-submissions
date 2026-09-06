class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_T = list(t)
        list_S = list(s)
        for char in s:
            if char in t:
                list_T.remove(char)
                list_S.remove(char)
        
        if list_T == [] and list_S == []:
            return True
        else:
            return False