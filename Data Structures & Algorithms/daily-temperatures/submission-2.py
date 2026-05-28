class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                print(f'stackT = {stackT}, stackInd = {stackInd}')
                print(f'\n res = {res}')

                res[stackInd] = i - stackInd
                print(f'res = {res} stackInd = {stackInd} res[stackInd] = {res[stackInd]}')

            stack.append((t,i))
            print(f'for t = {t} i = {i} stack = {stack}')
        return res