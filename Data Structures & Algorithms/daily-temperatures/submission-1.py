class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            print(f"Checking day {i}, temp = {temperatures[i]}")
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                results[prev_day] = i - prev_day
            stack.append(i)

        return results
