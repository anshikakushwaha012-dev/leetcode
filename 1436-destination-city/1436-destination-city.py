class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=[]
        for path in paths:
            start.append(path[0])
        for path in paths:
            if path[1] not in start:
                return path[1]