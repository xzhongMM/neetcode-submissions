class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        maxLength = 0

        for n in newNums:
            if n-1 not in newNums:
                #if it's starter, start counting
                curLength = 0
                while n in newNums:
                    curLength += 1
                    n += 1
                if curLength > maxLength:
                    maxLength = curLength

        return maxLength