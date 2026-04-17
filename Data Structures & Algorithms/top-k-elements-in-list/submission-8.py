from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        print(count)

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            
            if len(heap) > k:  #2 > 1
                heapq.heappop(heap)
                
        
        top_k_frequent = [num for freq, num in heap]
        return top_k_frequent