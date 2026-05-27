class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token not in "+-*/":
                res.append(int(token))
                print(f'if block res: {res} token {token}')
            else:
                b = res.pop()
                a = res.pop()
                print(f'else block res: {res} token {token} \n popped a & b {a,b}')

                if token == '+':
                    print('hey its addition man!!!')
                    res.append(a + b)
                elif token == '-':
                    print('hey its subtraction man!!!')
                    res.append(a - b)
                elif token == '*':
                    print('hey its multiplication man!!!')
                    res.append(a * b)
                elif token == '/':
                    print('hey its division man!!!')
                    res.append(int(a / b))
                                      
        return res[-1]
