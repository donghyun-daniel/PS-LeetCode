class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0 : return True
        planted_cnt = 0
        size = len(flowerbed)
        for idx in range(size):
            lower_idx, upper_idx = max(0, idx-1), min(idx+1, size-1)
            if not any(flowerbed[lower_idx:upper_idx+1]):
                planted_cnt += 1
                flowerbed[idx] = 1
            if planted_cnt == n:
                return True
        return False