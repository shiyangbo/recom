import numpy as np

def recom_ucf(u, N, train, W, k, m, n):
    '''对于给定用户u，推荐列表长度是固定的N。

    返回列表rank.
    '''
    rank = list()

    interacted_items = train[u].keys()

    ind = u - 1

    if np.sum(W[ind, :]) <= 1e-6:
        return rank

    # 找到k个最近邻用户
    ind_sort = np.argsort(W[ind, :])
    lst = list()
    for ind2 in range(m):
        v = ind_sort[ind2] + 1
        sim = W[ind, v - 1]
        lst.append((v, sim))
    near_vs = sorted(lst, key=lambda a: a[1], reverse=True)[: k]
    
    # 得到候选物品集re
    re = dict()
    for (v, sim) in near_vs:
        for i in train[v].keys():

            if i in interacted_items:
                continue
            else:

                if i not in re:
                    re.update({i: sim * train[v][i]})
                else:
                    re[i] += sim * train[v][i]

    len_re = len(re)

    if len_re >= N:
        i_w = sorted(re.items(), key=lambda a: a[1],
                reverse=True)[: N]
        rank = [i for (i, w) in i_w]
    else:
        i_w = sorted(re.items(), key=lambda a: a[1],
                reverse=True)
        rank = [i for (i, w) in i_w]

        count = 0
        st = interacted_items | re.keys()
        for ind2 in range(n):
            i = ind2 + 1

            if i in st:
                continue

            rank.append(i)
            count += 1

            if count == N:
                return rank

    return rank
