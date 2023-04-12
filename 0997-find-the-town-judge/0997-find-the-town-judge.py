class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_cands = {i+1 for i in range(n)}
        required_trust_cnt = {i+1: 0 for i in range(n)}
        
        for [f, t] in trust:
            if f in judge_cands:
                judge_cands.remove(f)
            required_trust_cnt[t] += 1
        if len(judge_cands) == 1:
            judge_cand = judge_cands.pop()
            if required_trust_cnt[judge_cand] == n-1:
                return judge_cand
            else:
                return -1
        else:
            return -1
            
            
            