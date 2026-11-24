import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        left, right = 0, len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            
            right -= 1
            left += 1
        
        return True