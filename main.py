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

train = {1: {1: 1, 2: 1, 4: 1},
        2: {2: 1, 3: 1, 4: 1},
        3: {5: 1, 6: 1, 7: 1, 8: 1},
        4: {3: 1, 8: 1},
        5: {1: 1, 6: 1, 7: 1}
}
test = {1: {7: 1},
        2: {8: 1},
        3: {3: 1},
        4: {6: 1},
        5: {2: 1}
}
m = 5
n = 8
'''

import sys
import read
import sim
import recom
import metric

script, file_path_train, file_path_test = sys.argv

#
(train, test, m, n) = read.read(file_path_train, file_path_test)
W = sim.sim_u(m, train)
(p, r) = metric.p_r(test=test, N=10, train=train, k=80, W=W, 
        m=m, n=n)
print(p, r)
