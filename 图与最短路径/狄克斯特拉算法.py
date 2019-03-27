# coding:utf-8
'''
使用狄克斯特拉算法找出加权图中前往X的最短路径

狄克斯特拉算法包含4个步骤。
(1) 找出最便宜的节点，即可在最短时间内前往的节点。
(2) 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销。
(3) 重复这个过程，直到对图中的每个节点都这样做了。
(4) 计算最终路径。

狄克斯特拉算法只适用于有向无环图，且不能将狄克斯特拉算法用于包含负权边的图
'''

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    # 正无穷：float("inf"); 负无穷：float("-inf")
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node   
    processed.append(node)
    node = find_lowest_cost_node(costs)
