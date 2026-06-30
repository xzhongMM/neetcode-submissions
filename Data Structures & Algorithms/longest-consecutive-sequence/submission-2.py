class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        newNums = set(nums)

        maxLength = 0
        starters = {}

        for n in newNums:
            if n-1 not in newNums:
                starters[n] = 0

        for n in starters:
            cur = n
            while cur in newNums:
                starters[n] += 1
                cur += 1
            maxLength = max(maxLength, starters[n])

        return maxLength