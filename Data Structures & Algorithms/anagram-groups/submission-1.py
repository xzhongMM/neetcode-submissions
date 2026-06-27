class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = defaultdict(list) #int[] -> String[]
        for str in strs:
            occurences = [0] * 26
            for letter in str:
                occurences[ord(letter) - ord("a")] += 1
            
            all_anagrams[tuple(occurences)].append(str)

        return list(all_anagrams.values())
            