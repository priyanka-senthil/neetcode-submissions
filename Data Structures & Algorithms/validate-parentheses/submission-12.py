class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parantheses = {"(": ")", "[": "]", "{": "}"}

        for ch in s:
            
            if ch in parantheses:
                stack.append(ch)
                # print(stack)
            else:
                if not stack:
                    return False
                element = stack.pop()

                if ch != parantheses[element]:
                    return False

        return len(stack) == 0