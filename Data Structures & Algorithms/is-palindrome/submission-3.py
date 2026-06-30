class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for letter in s:
            if letter.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                newS += letter.lower()

        left = 0
        right = len(newS)-1
        while left < right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        
        return True