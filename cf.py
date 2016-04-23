# -*- coding: utf-8 -*-

'''举个栗子.

   物品1   2   3   4   5   6   7   8

用户1  1   1   0   1   0   0  (1)  0
用户2  0   1   1   1   0   0   0  (1)
用户3  0   0  (1)  0   1   1   1   1
用户4  0   0   1   0   0  (1)  0   1
用户5  1  (1)  0   0   0   1   1   0

W =
         0    0.6667         0         0    0.3333
    0.6667         0         0    0.4082         0
         0         0         0    0.3536    0.5774
         0    0.4082    0.3536         0         0
    0.3333         0    0.5774         0         0
'''

import math

def u_sim(train):
    '''计算相似度矩阵.

    train是字典，形式为{user: {itm1, itm2, ...}}
    '''
    # build item_users table
    i_users = dict()

    # {
    #  itm1: {u1, u2, u3},
    #  itm2: {u1, u2, u3},
    #  itm3: {u1, u2, u3}
    # }

    for u, items in train.items():
        for i in items:

            if i not in i_users:
                i_users[i] = set()
            else:
                pass

            i_users[i].add(u)

    #
    deg = dict()
    up = dict()
    for i, users in i_users.items():
        for u in users:
            if u not in up:
                up.update({u: {}})

            # 计算用户度
            if u in deg:
                deg[u] += 1
            else:
                deg[u] = 1

            for v in users:

                if u == v:
                    continue
                else:

                    if v in up[u]:
                        up[u][v] += 1
                    else:
                        up[u][v] = 1

    #
    W = dict()
    for u, users in up.items():
        W.update({u: {}})

        for u2, num in users.items():
            var = num * 1.0 / math.sqrt(deg[u] * deg[u2])
            W[u].update({u2: var})

    return W

def recom_ucf(u, train, W, k):
    '''
    '''
    rank = dict()

    interacted_items = train[u]

    lst = sorted(W[u].items(), key=lambda a: a[1], reverse=True)[: k]
    for (v, sim) in lst:
        for i in train[v]:
            if i in interacted_items:
                continue
            else:
                if i in rank:
                    rank[i] += sim * 1 # note that rating  is all 1 not 1-5
                else:
                    rank.update({i: sim * 1})

    return rank

def i_sim(train):
    '''计算相似度矩阵.

    train是字典，形式为{user: {itm1:, itm2:, ...}}
    '''
    dic_1 = dict.fromkeys(train.keys(), []) 
    dic_2 = {}
    for u, itms in train.items():
        for itm in itms:
            pass

#
train = {1: {1, 2, 4},
    2: {2, 3, 4},
    3: {5, 6, 7, 8},
    4: {3, 8},
    5: {1, 6, 7}
}
W = u_sim(train)
rank = recom_ucf(2, train, W, k=10)
print(rank)
