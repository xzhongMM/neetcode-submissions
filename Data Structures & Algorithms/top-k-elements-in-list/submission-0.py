class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [] #list of tuples (frequency, number)
        visited = set()
        for i in range(len(nums)):
            n = nums[i]
            if n in visited:
                for f in range(len(freqs)):
                    if freqs[f][1] == n:
                        freqs[f] = (freqs[f][0]+1, n)
            else:
                freqs.append((1,n))
                visited.add(n)

        ans = []
        for num in sorted(freqs, reverse = True)[:k]:
            ans.append(num[1])
        
        return ans