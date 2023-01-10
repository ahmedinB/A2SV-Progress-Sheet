class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearestpointindex = -1
        nearestdistance = float("inf")
        for point in points :
            if point[0]!=x and point[1]!=y:
                continue
            if point[0]==x:
                distance = abs(y-point[1])
            elif point[1]==y:
                distance = abs(x-point[0])
            if distance < nearestdistance:
                nearestdistance = distance
                nearestpointindex = points.index(point)
        return nearestpointindex
