class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_occurences = {}
        for letter in s:
            if letter not in s_occurences:
                s_occurences[letter] = 0
            s_occurences[letter] += 1
        
        for letter in t:
            if letter not in s_occurences:
                return False
            s_occurences[letter] -= 1
            if s_occurences[letter] < 0:
                return False
            
        for l in s_occurences:
            if s_occurences[l] != 0:
                return False
        return True

#r:0
#a:0
#c:0
#e:0