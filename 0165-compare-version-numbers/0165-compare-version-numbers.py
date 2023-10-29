class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        from itertools import zip_longest
        v1 = list(map(int, version1.split("."))) 
        v2 = list(map(int, version2.split(".")))
        for r1, r2 in zip_longest(v1, v2, fillvalue=0):
            if r1 == r2:
                  continue
            else: return -1 if r1 < r2 else 1
        return 0