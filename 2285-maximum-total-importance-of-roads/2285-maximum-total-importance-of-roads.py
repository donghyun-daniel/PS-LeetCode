class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = Counter(city for road in roads for city in road)
        cities_by_degree = sorted(range(n), key=lambda x: degree.get(x, 0))
        values = {city: i + 1 for i, city in enumerate(cities_by_degree)}
        return sum(values[a] + values[b] for a, b in roads)