from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        heap = []

        for num, count in freq.items():
            if len(heap)<k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, num))
                    # heapq.heapreplace(heap, (num, count))

        return [num for count, num in heap]
        