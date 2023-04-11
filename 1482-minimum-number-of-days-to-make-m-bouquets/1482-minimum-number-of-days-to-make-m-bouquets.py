class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def getNumOfBouquets(targetDate: int) -> int:
            bouquet_cnt, flower_cnt = 0, 0
            for day in bloomDay:
                if day <= targetDate:
                    flower_cnt += 1
                else:
                    flower_cnt = 0
                if flower_cnt == k:
                    flower_cnt = 0
                    bouquet_cnt += 1
            return bouquet_cnt
        
        if len(bloomDay) < m * k: return -1 
        l,r = 1, max(bloomDay)
        while l <= r:
            mid = l + (r - l)//2 
            if getNumOfBouquets(targetDate=mid) >= m:
                r = mid - 1 
            else:
                l = mid + 1
        return l
        
        
            
            