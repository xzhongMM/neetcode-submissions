class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        all_anagrams = []
        index = 0
        for str in strs:
            occurences = {}
            for letter in str:
                if letter not in occurences:
                    occurences[letter] = 0
                occurences[letter] += 1
            if occurences not in all_anagrams:
                answer.append([str])
                all_anagrams.append(occurences)
                index += 1
            else:
                answer[all_anagrams.index(occurences)].append(str)

        return answer
            