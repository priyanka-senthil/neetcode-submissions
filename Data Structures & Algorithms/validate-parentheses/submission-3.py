class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(' : ')', '[':']', '{':'}'}

        for char in s:
            print(f'char {char} s {s}')
            if char in pairs:
                print(f'char in if {char}')
                stack.append(char)
            elif not stack or pairs[stack.pop()]!= char:
                return False
        
        return not stack