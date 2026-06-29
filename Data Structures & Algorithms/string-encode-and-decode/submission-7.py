class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        return str(len(strs[0])) + "#" + strs[0] + self.encode(strs[1:])

    def decode(self, s: str) -> List[str]:
        answer = []

        size = 0
        while s:
            if s[0] in "0123456789":
                size = (size*10) + int(s[0])
                s = s[1:]
                continue
            if s[0] == '#' and size != 0:
                word = s[1:size+1]
                answer.append(word)
                s = s[size+1:]
                size = 0
                continue
            if s[0] == "#" and size == 0:
                answer.append("")
                s = s[1:]
        
        return answer