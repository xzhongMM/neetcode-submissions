class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1]*len(nums)
        for i in range(1, len(nums)):
            #calculate product before i
            before[i] *= before[i-1] * nums[i-1]

        after = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            #calculate product after i
            after[i] *= after[i+1] * nums[i+1]

        answer = [1]*len(nums)
        for a in range(len(nums)):
            answer[a] = before[a] * after[a]

        return answer