class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for i in strs:
           enc_str += i+"!"

        print(enc_str)

        return enc_str 

    def decode(self, s: str) -> List[str]:
        return s.split("!")[:-1]


        # return ["Bob"]