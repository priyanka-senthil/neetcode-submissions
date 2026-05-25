class Solution:
    def isValid(self, s: str) -> bool:
        if not s: 
            return False

        my_dict = { '[' : ']', '{' : '}', '(': ')'}
        # close_brackets = [')', '}', ']']
        res = []

        for ch in s:
            if ch in my_dict:
                res.append(ch)
            else:
                if not res:
                    return False
                a = res.pop()
                if ch != my_dict[a]:
                    return False
            
        return len(res) == 0


        