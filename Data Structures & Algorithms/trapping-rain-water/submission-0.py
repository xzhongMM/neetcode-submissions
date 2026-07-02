class Solution:
    def trap(self, height: List[int]) -> int:
        #0, 1, 5, 5, 5
        #5, 4, 4, 4, 0
        prefixMax = [0]
        suffixMax = []
        size = len(height)

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

        print(prefixMax)
        print(suffixMax)
        print(height)
        total = 0
        for i in range(len(height)):
            water = min(prefixMax[i], suffixMax[i]) - height[i]
            if water > 0:
                total += water

        return total
