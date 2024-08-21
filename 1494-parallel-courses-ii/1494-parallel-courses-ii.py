class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prereqs = [0] * n
        for prev, next in relations:
            prereqs[next - 1] |= 1 << (prev - 1)
                                       
        queue = deque([(0, 0)])  # taken courses bitmask, semester cnt
        visited = set()
        
        while queue:
            taken, semester = queue.popleft()
            if taken == (1 << n) - 1:  # All courses taken
                return semester
            
            # Find avail courses
            available = 0
            for i in range(n):
                if not (taken & (1 << i)) and (taken & prereqs[i]) == prereqs[i]:
                    available |= 1 << i
            
            # Try all combinations of up to k avail courses
            subset = available
            while subset:
                if bin(subset).count('1') <= k:
                    new_taken = taken | subset
                    if new_taken not in visited:
                        visited.add(new_taken)
                        queue.append((new_taken, semester + 1))
                subset = (subset - 1) & available
        
        return -1