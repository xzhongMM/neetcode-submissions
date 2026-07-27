class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = 1

        s1freqs = [0]*26
        for s in s1:
            s1freqs[ord(s) - 97] += 1

        s2freqs = [0]*26

        while right <= len(s2):
            #update freq of new character
            s2freqs[ord(s2[right-1]) - 97] += 1
            #if substrings not of len(s1), increment right
            while right - left < len(s1):
                right += 1
                s2freqs[ord(s2[right-1]) - 97] += 1
            #if it's correct length, check if two freq lists match
            if s1freqs == s2freqs:
                return True
            else:
                #if not increment left and right and update frequenciy of left character
                s2freqs[ord(s2[left]) - 97] -= 1
                left += 1
                right += 1
        return False
            
