class Solution:
    def isValid(self, s: str) -> bool:

        l = []
        for bracket in s:
            print(bracket)
            if bracket in "({[":
                # print("in-if")
                l.append(bracket)
            elif bracket in ")}]":
                # print("in elif")
                try:
                    if (bracket == ")" and l[-1] == "(") or (bracket == "}" and l[-1] == "{") or (bracket == "]" and l[-1] == "["):
                        l.pop()
                except:
                    return False
        
        if l == []:
            return True
        else:
            return False