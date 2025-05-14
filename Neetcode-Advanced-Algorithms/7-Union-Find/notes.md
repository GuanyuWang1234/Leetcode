# Union Find 

## Purpose
- Keeping track of the nodes that are connected
- Detecting cycles

DFS: does this, but only efficient for static graph.
Union-Find: Also efficient for dynamic graph(adding edges overtime)

## Concept
For each edge, if boths nodes share the same root, then there's a cycle. Otherwise, set the node with the higher rank to be the other node's parent

## Time Complexity
Find takes O(1) with union by rank and path compression. 
With m edges, total = O(m)

## Implementation

### Setup
```python
class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
```

### Find
Path Compression: set the parent of a node to the root of the node
```python
def find(self, n):
    if self.par[n] != n:
        self.par[n] = self.find(self.par[n])

    return self.par[n]
```

### Union
```python
def union(self, n1, n2):
    p1, p2 = self.find(n1), self.find(n2)

    if p1 == p2:
        return False

    if self.rank[p1] > self.rank[p2]: 
        self.par[p2] = p1
    elif self.rank[p1] < self.rank[p2]: 
        self.par[p1] = p2
    else:
        self.par[p2] = p1
        self.rank[p1] += 1
    return True 
```