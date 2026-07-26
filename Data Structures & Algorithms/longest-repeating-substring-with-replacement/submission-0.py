class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        freq_list = defaultdict(int)
        maxLen = 0
        maxFreq = 0
        while right <= len(s):
            lastChar = s[right-1]
            freq_list[lastChar] += 1
            maxFreq = max(maxFreq, freq_list[lastChar])
            while not (right - left - maxFreq) <= k:
                freq_list[s[left]] -= 1
                left += 1
            maxLen = right - left
            right += 1
        
        return maxLen