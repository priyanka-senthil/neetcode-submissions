class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        print(f"s = {s}")
        t = sorted(t)
        print(f"t = {t}")
        if len(s) == len(t):
            if s == t:
                return True
        return False
                

        