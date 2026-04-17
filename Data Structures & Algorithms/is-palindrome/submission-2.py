import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        striped_word = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(striped_word)
        
        reverse_word = striped_word[::-1]

        for a, b in zip(striped_word, reverse_word):
            if a == b:
                continue
            else:
                return False
        return True
