class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum())
        s = s.lower()
        j = len(s) - 1
        
        for i in range(len(s)):   #i 0 to 6
            if len(s) != 0 and i != j and i < j : #i = 0 & j = 6
                print(f"s[i] {s[i]} \n s[j] {s[j]}")
                if s[i] == s[j]:
                    print(f"if s[i] == s[j] :  s[i] {s[i]} s[j] {s[j]}")
                    j -= 1
                else:
                    return False
        return True

        