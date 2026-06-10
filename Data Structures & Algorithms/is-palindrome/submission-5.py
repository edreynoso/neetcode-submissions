import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0

        s = re.findall("\w", s, re.ASCII)
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l +=1
            if not s[r].isalnum():
                r -=1

            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            else:
                l +=1
                r -=1
        
        return True