class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths=[path[::-1] for path in paths]
        for i in range(len(paths)):
            if paths[i][0] not in [path[1] for path in paths]:
                return paths[i][0]