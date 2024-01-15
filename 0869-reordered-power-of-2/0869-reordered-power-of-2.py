class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = []
        comparator = sorted(str(n))
        power_of_two = 1
        for _ in range(0, 31):
            if comparator == sorted(str(power_of_two)):
                return True
            power_of_two *= 2
        return False