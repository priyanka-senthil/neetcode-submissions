class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token not in "+-*/":
                res.append(int(token))
                print(f'res: {res} token {token}')
            else:
                b = res.pop()
                a = res.pop()
                print(f'res in else: {res} token {token}')

                if token == '+':
                    res.append(a + b)
                elif token == '-':
                    res.append(a - b)
                elif token == '*':
                    res.append(a * b)
                elif token == '/':
                    res.append(int(a / b))
                                      
        return res[-1]
