class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            # print(i, n)
            diff = target - n
            print(f'for i={i} and n={n} and diff={diff}')
            if diff in hashMap:
                print(f'hashMap ={hashMap} {[hashMap[diff], i]}')
                return [hashMap[diff], i]
            hashMap[n] = i
        return
