class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers) - 1
#target = 3
        while l < r: # 0<3 || 0<2 || 0<1
            curSum = numbers[l] + numbers[r]  #1 + 4 = 5 || 1+3 = 4 || 1 + 2 = 3
            print(f"curSum = {curSum}")
            if curSum > target:     #5 > 3 || 4>3 || 3>3
                r -= 1              # r = 2 || r = 1 
            elif curSum < target:   # 3 < 3
                l += 1
            else:
                return [l+1, r+1]  # 0+1 = 1, 2