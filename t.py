# -*- coding: utf-8 -*-
"""
"""

import random

N = 2
n = 5

u = 2
train = {1: {3}}
test = {1: {1, 4}}

#
total_items = set()
for i in range(n):
    item = i + 1
    total_items.add(item)

rs = 0.0
count = 0
for u in test:
    items = test[u]

    rank_items = [1, 2]
    # 将列表变为字典，存储索引位置
    rank_items_dic = dict()
    ind = 0
    for item in rank_items:
        ind += 1
        rank_items_dic.update({item: ind})

    len_unchoosed = n - len(train[u])

    in_rlist = items & rank_items_dic.keys()

    not_in_rlist = items - rank_items_dic.keys()
    # 其它物品的索引位置
    situation = random.sample(range(N + 1, len_unchoosed + 1),
            len(not_in_rlist))
    other_items_dic = dict()
    ind = 0
    for item in not_in_rlist:
        other_items_dic.update({item: situation[ind]})
        ind += 1

    print(rank_items_dic, other_items_dic)
