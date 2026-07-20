class Solution:
    def canFinish(self, k: int, piles: List[int], h: int) -> bool:
        count = 0
        for p in piles:
            count += math.ceil(p/k)

        return count <= h
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1

        while lower < upper:
            mid = (lower + upper) // 2
            if self.canFinish(mid, piles, h):
                upper = mid
            else:
                lower = mid + 1

        return upper
        