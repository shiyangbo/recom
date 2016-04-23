# -*- coding: utf-8 -*-

'''
'''

import numpy as np
import math

def sim_u(m, train):
    '''返回用户的相似矩阵W, m*m dimension.
    '''
    W = np.zeros((m, m), dtype=np.float64)

    # 计算用户的相似矩阵W
    for ind in range(m):
        u = ind + 1

        if u not in train:
            continue

        for ind2 in range(m):
            v = ind2 + 1

            if ind2 == ind:
                continue

            if v not in train:
                continue

            u_items = train[u]
            v_items = train[v]
            hit = len(u_items.keys() & v_items.keys())

            if hit == 0:
                continue
            else:
                var = hit * 1.0 / math.sqrt(len(u_items)
                        * len(v_items))
                W[ind][ind2] = var
                W[ind2][ind] = var

    return W
