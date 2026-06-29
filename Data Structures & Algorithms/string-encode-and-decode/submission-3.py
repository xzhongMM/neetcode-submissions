class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        return strs[0] + ", ," + self.encode(strs[1:])

    def decode(self, s: str) -> List[str]:
        strs = s.split(", ,")
        return strs[:len(strs)-1]