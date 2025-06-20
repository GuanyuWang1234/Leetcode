# Redundant Connection

## Problem Statement

Graph *edges* is a tree with *n* nodes, with 1 additional edge added. 
Return an edge, when removed, results in a tree.

## DFS Brute Force

Start with an empty Adj list.
For each edge = [source, target], run DFS on the adj list to see if source can reach target. If so, there's a graph and we return edge. 
Otherwise, add edge to adj list and keep going.
