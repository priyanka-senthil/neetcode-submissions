class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # nums = [1,2,2,3,3,3], k = 2
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            print(f"for n {n} the count is {count}")
        for n, c in count.items():
            freq[c].append(n)
            print(f"for values n {n} and c {c} the freq is {freq}")

        res = []

        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        