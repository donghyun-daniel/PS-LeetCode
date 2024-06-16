class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in words:
            anagram[''.join(sorted(word))].append(word)
        return anagram.values()