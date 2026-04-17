from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = {}
        count = Counter(nums)
        heap = []
        print(count.items())
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            print(heap)
            print(len(heap))
            if len(heap) > k:
                heapq.heappop(heap)
        
        top_k_frequent = [num for freq, num in heap]
        print(f"top_k_frequent {top_k_frequent}")
        return top_k_frequent