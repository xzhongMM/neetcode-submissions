import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        for i in range(len(nums)):
            product = math.prod(nums[:i]) * math.prod(nums[i+1:])
            answer[i] *= product

        return answer
