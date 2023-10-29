class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        from itertools import zip_longest
        v1, v2 = version1.split("."), version2.split(".")
        for r1, r2 in zip_longest(v1, v2, fillvalue=0):
            if int(r1) < int(r2):
                return -1
            elif int(r1) > int(r2):
                return 1
            else:
                continue
        return 0