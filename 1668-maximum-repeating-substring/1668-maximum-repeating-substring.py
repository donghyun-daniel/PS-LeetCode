class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence_size = len(sequence)
        word_size = len(word)
        max_k = sequence_size // word_size
        for k in reversed(range(0, max_k+1)):
            if k*word in sequence:
                return k
        return 0
            