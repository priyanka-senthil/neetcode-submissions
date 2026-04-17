class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s = sorted(s)
        t = sorted(t)
        if s_len == t_len:
            if s == t:
                return True
        return False
                

        