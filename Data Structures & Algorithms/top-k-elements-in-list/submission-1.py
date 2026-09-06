class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = Counter(nums).most_common(k)
        print(type(dic))
        print(dic)

        res = []
        for i in dic:
            res.append(i[0])
        
        return res