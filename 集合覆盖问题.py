# coding:utf-8

# 创建一个列表，其中包含要覆盖的州。传入一个数组，它被set()转换为集合
# 集合类似于列表，只是同样的元素只能出现一次，即集合不能包含重复的元素。
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

# 还需要有可供选择的广播台清单，我选择使用散列表来表示它。
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])



# 最后，需要使用一个集合来存储最终选择的广播台。
final_stations = set()

while states_needed:
    # 你需要遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台。
    # 我将这个广播台存储在best_station中。
    best_station = None
    # states_covered是一个集合，包含该广播台覆盖的所有未覆盖的州。
    states_covered = set()
    # for循环迭代每个广播台，并确定它是否是最佳的广播台。
    for station, states_for_station in stations.items():
        # a&b表示a和b的交集，ａ|b表示ａ和ｂ的并集，ａ－ｂ表示ａ和ｂ的差集
        # coverd 包含当前广播台覆盖的一系列还未覆盖的州 
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            # 将best_station设置为当前广播台
            best_station = station
            states_covered = covered

states_needed -= states_covered
final_stations.add(best_station)

print final_stations