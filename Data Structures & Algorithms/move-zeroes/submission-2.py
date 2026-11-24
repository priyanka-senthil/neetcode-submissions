class Solution:
    def moveZeroes(self, numbers: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0

        for i in range(len(numbers)):
            if numbers[i] != 0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                j += 1
        
        return numbers
        