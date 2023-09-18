class Solution:
    def partitionString(self, input: str) -> int:
        tmp = ""
        cnt = 0
        for s in input:
            if s in tmp:
                tmp = s
                cnt += 1
            else:
                tmp += s
        if tmp:
            cnt += 1
        return cnt