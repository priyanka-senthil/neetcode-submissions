from typing import List

class Solution:

    def __init__(self):
        self.stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            if token.isdigit() or (len(token) > 1 and token[0] == '-'):  # Handles positive and negative numbers
                self.stack.append(int(token))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if token == '+':
                    self.stack.append(a + b)
                elif token == '-':
                    self.stack.append(a - b)
                elif token == '*':
                    self.stack.append(a * b)
                elif token == '/':
                    self.stack.append(int(a / b))  # Ensures integer division
        return self.stack[0]  # Return the result as an integer

# Example usage:
solution = Solution()
result = solution.evalRPN(["2", "1", "+", "3", "*"])
print(result)  # Output: 9
