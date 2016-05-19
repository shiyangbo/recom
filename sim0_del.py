def u_sim(train):
    '''利用倒排表，计算用户的相似度矩阵.

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
