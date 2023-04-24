class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from functools import reduce
        from collections import Counter
        freqs = [item[1] for item in Counter(nums).items()]
        if len(freqs) < 3:
            return 0
        else:
            triplets_combination = list(itertools.combinations(freqs, 3))
            total_product = sum(
                [
                    reduce(
                        (lambda x, y: x * y), sublist
                    ) for sublist in triplets_combination
                ]
            )
            return total_product