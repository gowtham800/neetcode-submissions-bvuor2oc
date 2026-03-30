from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        most_freq = counts.most_common(k)

        return [pair[0] for pair in most_freq]
