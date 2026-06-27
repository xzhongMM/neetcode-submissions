class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = defaultdict(list) #int[] -> String[]
        for str in strs:
            sorted_str = ''.join(sorted(str))
            all_anagrams[sorted_str].append(str)

        return list(all_anagrams.values())
            