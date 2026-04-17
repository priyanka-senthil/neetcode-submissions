from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize the left and right product lists
        left = [1] * n
        print(left)
        right = [1] * n
        output = [0] * n

        # Fill the left array
        # left[i] will be the product of all nums[j] where j < i
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        print(left)

        # Fill the right array
        # right[i] will be the product of all nums[j] where j > i
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(right)

        # Construct the output array
        # output[i] will be the product of left[i] and right[i]
        for i in range(n):
            output[i] = left[i] * right[i]

        return output
