class Solution:
    def is_connected(self, src, target, visited, adj_list) -> bool:
        if src == target:
            return True

        visited[src] = True

        is_found = False

        for node in adj_list[src]:
            if visited[node] == False:
                is_found = is_found or self.is_connected(node, target, visited, adj_list)

        return is_found
                
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        adj_list = [[] for _ in range(N + 1)]

        for edge in edges:
            visited = [False] * (N + 1)

            if self.is_connected(
                edge[0], edge[1], visited, adj_list):
                return edge

            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        return []

