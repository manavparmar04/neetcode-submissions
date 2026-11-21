class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for index, i in enumerate(nums):
            target_value = target - i

            if target_value in hash_map:
                return [hash_map[target_value],index]
            else:
                hash_map[i] = index
                    
