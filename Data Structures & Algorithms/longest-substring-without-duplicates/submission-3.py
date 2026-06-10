class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 1:
            return 0
        
        seen = set()
        
        l = 0
        r = 0

        length = 1
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r +=1
            else:
                seen.remove(s[l])
                l +=1
            length = max(length, (r-l))
        return length 