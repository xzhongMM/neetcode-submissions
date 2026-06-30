class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        maxLength = 0
        starters = {}

        for n in nums:
            if n-1 not in nums:
                starters[n] = 0

        for n in starters:
            cur = n
            while cur in nums:
                starters[n] += 1
                cur += 1
            maxLength = max(maxLength, starters[n])

        return maxLength