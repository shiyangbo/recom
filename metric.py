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
