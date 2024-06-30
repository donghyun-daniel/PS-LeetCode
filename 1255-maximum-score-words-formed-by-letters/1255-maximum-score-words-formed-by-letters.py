from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_cnt = Counter(letters)
        word_scores = [sum(score[ord(c) - ord('a')] for c in word) for word in words]
        
        def is_creatable(word, letter_cnt):
            return all(letter_cnt[c] >= word.count(c) for c in set(word))
        
        def backtrack(idx, current_letter_cnt):
            if idx >= len(words):
                return 0
            
            max_score = backtrack(idx + 1, current_letter_cnt)
            
            # Use current word if possible
            if is_creatable(words[idx], current_letter_cnt):
                new_letter_cnt = current_letter_cnt.copy()
                for c in words[idx]:
                    new_letter_cnt[c] -= 1
                max_score = max(
                    max_score, word_scores[idx] + backtrack(idx + 1, new_letter_cnt)
                )
            
            return max_score
        
        return backtrack(0, letter_cnt)