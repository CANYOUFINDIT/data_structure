# coding:utf-8
import Queue

# 广度优先遍历
def bfs(adj, start):
    visited = set()
    q = Queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
 
# 深度优先
def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])
 
 
graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)