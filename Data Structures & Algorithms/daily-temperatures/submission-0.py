class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        i = 0
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                   # print(f"Day {i}: wait {j - i} days for a warmer temp ({temperatures[j]})")
                    results.append(j-i)
                    found = True
                    break
            if not found:
                results.append(0)
        return results
    