# -*- coding: utf-8 -*-

def read(file_path_train, file_path_test):
    '''
    '''
    train = dict()
    test = dict()
    m = 0
    n = 0
    with open(file_path_train, 'r') as train_file:
        for row in train_file.readlines():
            r = row.strip().split('\t')
            u = int(r[0])
            i = int(r[1])

            if u > m:
                m = u

            if i > n:
                n = i

            if u in train:
                train[u].update({i: 1})
            else:
                train.update({u: {i: 1}})

    with open(file_path_test, 'r') as test_file:
        for row in test_file.readlines():
            r = row.strip().split('\t')
            u = int(r[0])
            i = int(r[1])

            if u > m:
                m = u

            if i > n:
                n = i

            if u in test:
                test[u].update({i: 1})
            else:
                test.update({u: {i: 1}})

    # 数据集完整性
    len_test = len(test)
    len_train = len(train)
    if len_test > len_train:
        train.update(dict.fromkeys(test.keys() - train.keys(), dict()))

    return (train, test, m, n)
