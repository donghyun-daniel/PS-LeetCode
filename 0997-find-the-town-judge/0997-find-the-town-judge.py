class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from collections import defaultdict
        cands = defaultdict(int)
        for i in range(n):
            cands[i+1] = 0
        for [f, t] in trust:
            if f in cands:
                cands.pop(f)
            if t in cands:
                cands[t] += 1
        if cands:
            for cand in cands:
                if cands[cand] == n-1:
                    return cand
                else:
                    return -1
        else:
            return -1
            
        