class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            print(f" decoded result = {res}")
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(f"length of s = {len(s)}")
        
        while i < len(s): 
            j = i     # j = 0, j = 4
            while s[j] != "#": #s[0] = 2, s[1] = #, s[4] = 3, s[5] = #
                j += 1   # j = 1, j = 5
            length = int(s[i:j]) # s[0:1]  => length = 2, s[4:5] = length = 3
            res.append(s[j + 1 : j + 1 + length]) # res => s[1+1: 1+1+2 ] s[2:4] => res = "we"
            # res => s[6 : 9] => "say"
            i = j + 1 + length #i = 4, i = 5+1+3 = 9 
            print(f"i value = {i}")  
#| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
#|-------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|
#| Value | 2 | # | w | e | 3 | # | s | a | y | 1 | #  | :  | 3  | #  | y  | e  | s  | 0  | 1  | 2  |

        return res
