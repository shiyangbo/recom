import numpy as np

def recom_ucf(u, N, train, W, k, m, n):
    '''对于给定用户u，推荐列表长度是固定的N。

    返回列表rank.
    '''
    rank = []

    interacted_items = train[u].keys()

    user_ind = u - 1

    if np.sum(W[user_ind, :]) <= 1e-6: 
        ## 随机选N个填充推荐列表
        #st = interacted_items
        #for ind2 in range(n):
        #    item = ind2 + 1

        #    if item in st:
        #        continue
        #    else:
        #        rank.append(item)

        #rank = rank[: N]
        #return rank

        # 法2，返回空列表
        return rank

    # 找到k个最近邻用户, nera_users
    ind_sort = np.argsort(W[user_ind, :])
    lst = list()
    for ind2 in range(m):
        other_user = ind_sort[ind2] + 1
        sim = W[user_ind, other_user - 1]
        lst.append((other_user, sim))
    near_users = sorted(lst, key=lambda a: a[1], reverse=True)[: k]
    
    # 得到候选物品集items
    items = dict()
    for (other_user, sim) in near_users:
        for i in train[other_user].keys():

            if i in interacted_items:
                continue

            if i not in items:
                items.update({i: sim * train[other_user][i]})
            else:
                items[i] += sim * train[other_user][i]

    len_items = len(items)

    if N > (n - len(interacted_items)):
            N = n - len(interacted_items) # 推荐列表长度最大为该用户在train中未选择过的商品集合

    if len_items >= N:
        i_w = sorted(items.items(), key=lambda a: a[1],
                reverse=True)[: N]
        rank = [i for (i, w) in i_w]
        return rank
    else:
        i_w = sorted(items.items(), key=lambda a: a[1],
                reverse=True)
        rank = [i for (i, w) in i_w]

        st = interacted_items | items.keys()

        count = 0
        end = N - len(rank)
        for ind2 in range(n):
            i = ind2 + 1

            if i in st:
                continue

            rank.append(i)
            count += 1

            if count == end:
                return rank
        
        print('error. in recom.py')
        exit(0)

