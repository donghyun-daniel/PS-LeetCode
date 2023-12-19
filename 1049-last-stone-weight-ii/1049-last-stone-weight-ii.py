class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums = set([0])
        for stone in stones:
            tmp = set([])
            for s in sums:
                tmp.add(abs(s + stone))
                tmp.add(abs(s - stone))
            sums = tmp
        return min(sums) if sums else 0