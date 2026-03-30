class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, n in enumerate(nums):
            difference = target - n
            if difference in hash_map:
                return [hash_map[difference], idx]
            hash_map[n] = idx