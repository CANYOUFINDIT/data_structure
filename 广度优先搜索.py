# coding:utf-8
'''
问题： 从朋友中找到一名芒果销售商，如果自己的朋友中没有芒果销售商，则从朋友的朋友中找与自己关系最近的芒果销售商
解法： 人际关系是图的结构，使用队列来完成广度优先搜索，找到与自己关系最近的芒果销售商
'''
# 导入队列
from collections import deque

graph = {}
# 你和你的朋友们，名字结尾为m的人是芒果销售商
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 判断是不是芒果销售商
def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # 建立一个双端队列
    search_queue = deque()
    # 将邻居都加到队列里
    search_queue += graph[name]
    # 记录检查过的人
    searched = []
    # 如果队列不为空
    while search_queue:
        # 将队列中的第一个人取出
        person = search_queue.popleft()
        # 如果没被检查过
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller!"
                return True
            else:
                # 将这个人的朋友加入队列
                search_queue += graph[person]
                # 将这个人标记为检查过
                searched.append(person)
    return False

search("you")

'''
如果你在你的整个人际关系网中搜索芒果销售商，就意味着你将沿每条边前行（记住，边是从一个人到另一个人的箭头或连接），因此运行时间至少为O(边数)。
你还使用了一个队列，其中包含要检查的每个人。将一个人添加到队列需要的时间是固定的，即为O(1)，因此对每个人都这样做需要的总时间为O(人数)。
所以，广度优先搜索的运行时间为O(人数+ 边数)，这通常写作O(V + E)，其中V为顶点（vertice）数，E为边数。
'''