import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ""

#         for char in s:
#             if char.isalnum():
#                 cleaned += char.lower()
        
#         left, right = 0, len(cleaned) - 1

#         while left < right:
#             if cleaned[left] != cleaned[right]:
#                 return False
            
#             right -= 1
#             left += 1
        
#         return True

# -------------------without using cleaned--------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalnum():  # if not an alphanumberic character increament the left pointer and continue the loop for eg if , comes left pointer is incremented and skips the rest of the code and continues the loop
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True