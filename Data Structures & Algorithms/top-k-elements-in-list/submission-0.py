class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = Counter(nums).most_common(k)



        return list(dic.values())