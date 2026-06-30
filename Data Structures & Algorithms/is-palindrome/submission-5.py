class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for letter in s:
            if letter.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                newS += letter.lower()
        size = len(newS)

        return newS[0:size//2] == newS[size-1:(size-1)//2:-1]