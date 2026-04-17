class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):   # i= 0,n= 3 || i =1,n=4
            diff = target - n  # target = 7 diff = 7 -3 = 4 || 7-4 = 3
            if diff in prevMap: #if 4 in {} || if 3 in {3:0}
                print(n, prevMap)
                return [prevMap[diff], i]  # [0,1]
            prevMap[n] = i #prevMap {3: 0,}
