import random
import recom

def p_r(test, N, train, k, W, m, n):
    '''N是推荐列表长度。

    返回（准确率，召回率）.
    '''
    precision = 0.0
    recall = 0.0
    count = 0
    for u in test.keys():
        test_items = test[u].keys()

        rank_items = recom.recom_ucf(u, N, train, W, k, m, n)

        up = len(test_items & set(rank_items))

        precision += up * 1.0 / N
        recall += up * 1.0 / len(test_items)
        count += 1
        print("test中第{0}个用户".format(count))

    return (precision / count, recall / count)

def rs(test, N, train, k, W, m, n):
    '''N是推荐列表长度，m是用户总数，n是物品总数。

    特别的，要求N=n。
    '''
    # 物品全集
    total_items = set()
    for i in range(m):
        item = i + 1
        total_items.add(item)

    rs = 0.0
    count = 0
    for u in test:
        items = test[u].keys()
        len_unchoosed = n - len(train[u])

        rank_items = recom.recom_ucf(u, N, train, W, k, m, n)

        # 若无推荐，则跳过
        if len(rank_items) == 0:
            continue

        # 将列表变为字典，存储索引位置
        rank_items_dic = dict()
        ind = 0
        for item in rank_items:
            ind += 1
            rank_items_dic.update({item: ind})

        # 计算rs
        for item in items:

            if item in rank_items_dic:
                rs += rank_items_dic[item] / len_unchoosed
                count += 1
            else:
                print('omit')

    return rs / count
