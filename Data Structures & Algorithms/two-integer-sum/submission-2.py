class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return None


        # 2,1,5,3
        # target =4
        hash_m = {}

        for i in range(len(nums)):
            if (target-nums[i]) in hash_m:
                return ([hash_m[target-nums[i]],i])
            else:
                hash_m[nums[i]] = i
        
        return None
