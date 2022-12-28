Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i, 0<=i

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Approach -> 
1. Make a adjacency list to store node and dist in pairs
2.Create a distance vector with initial distance as infinite
3.For source node its distance is 0
4.Declare a que and append src node in it.
5.Now traverse in the que until it is not empty

from typing import List
from collections import deque,defaultdict
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i,j,k in edges:
            adj[i].append([j,k])
        dist = [float('inf')]*n
        dist[0] = 0
        que = deque()
        que.append(0)
        
        while que:
            node = que.popleft()
            if node in adj:
                for ngh,dis in adj[node]:
                    if dist[node]+dis < dist[ngh]:
                        dist[ngh] = dist[node]+dis
                        que.append(ngh)
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist
