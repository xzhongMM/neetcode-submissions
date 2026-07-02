class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = [0]
        suffixMax = []

        curMax = height[0]
        for h in height[1:]:
            prefixMax.append(curMax)
            if h > curMax:
                curMax = h

        curMax = 0
        for h in height[::-1]:
            suffixMax.insert(0,curMax)
            if h > curMax:
                curMax = h

        total = 0
        for i in range(len(height)):
            water = min(prefixMax[i], suffixMax[i]) - height[i]
            if water > 0:
                total += water

        return total
