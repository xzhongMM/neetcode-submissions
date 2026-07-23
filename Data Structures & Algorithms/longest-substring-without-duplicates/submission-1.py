class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        current_longest = 0
        backup = 0
        while r <= len(s):
            sub = s[l:r]
            if len(set(sub)) != len(sub):
                l += 1
                backup -= 1
            else:
                backup += 1
                current_longest = max(current_longest, backup)
                r += 1
        
        return current_longest
