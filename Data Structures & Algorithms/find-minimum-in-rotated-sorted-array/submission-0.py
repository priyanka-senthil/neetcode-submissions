class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            print(f'for l = {l} and r = {r}')
            if nums[l] < nums[r]:
                print(f'nums[l] = {nums[l]} and nums[r] = {nums[r]} condition passed')
                res = min(res, nums[l])
                print(f'res = {res}')
                break
            else:
                print(f'nums[l] = {nums[l]} and nums[r] = {nums[r]} condition failed')

            m = (l + r) // 2
            print(f'm = {m}')
            res = min(res, nums[m])
            print(f'res = {res}')

            if nums[m] >= nums[l]:
                l = m + 1
                print(f'l= {l}')

            else:
                r = m - 1
                print(f'r= {r}')
        return res