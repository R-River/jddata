# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 11:58:34 2017

@author: Administrator
"""
import pandas as pd
import sys
reload(sys)

sys.setdefaultencoding('utf-8')


def load_data(file_name):
    """read files"""
    with open(file_name) as f:
        head = f.readline().strip().strip('\xef\xbb\xbf').split(',')
        pass

    tb = pd.read_table(file_name, sep=',')
    tb = tb.rename(columns={tb.columns[0]: head[0]})

    return tb


def recall(df, col):
    """calculate recall"""
    tp = float(sum(df[col]))
    fn = float(len(df)-len(df[df['sku_id_x'] > 0]))
    return round(tp/(tp+fn), 4)


def precision(df, col):
    """calculate precision"""
    tp = float(sum(df[col]))
    a = df['sku_id_x'] > 0
    b = (df[col] == 0)
    fp = float(len(df[a & b]))
    return round(tp/(tp+fp), 4)


def score(label_recall, label_precision, pred_recall, pred_precision):
    """
    Score=0.4*F11 + 0.6*F12
    F11=6*label_recall*label_precision/(5*label_recall+label_precision)
    F12=5*pred_recall*pred_precision/(2*pred_recall+3*pred_precision)
    """
    f11 = 6*label_recall*label_precision/(5*label_recall+label_precision)
    f12 = 5*pred_recall*pred_precision/(2*pred_recall+3*pred_precision)

    return 0.4*f11 + 0.6*f12


if __name__ == '__main__':

    target = load_data('F:\jdData\\target0410_0415.csv')  # target file has 2 columns: user_id, sku_id
    output = load_data('F:\jdData\output.csv')  # output file has 2 columns: user_id, sku_id
    # init judgement columns
    output['label'] = 0
    output['pred'] = 0

    combine = pd.merge(output, target, how='outer', on='user_id')
    combine['sku_id_y'] = combine[combine['sku_id_y'] > 0]['sku_id_y'].astype(int).astype(str)
    combine['user_id'] = combine[combine['user_id'] > 0]['user_id'].astype(int).astype(str)
    combine['sku_id_x'] = combine[combine['sku_id_x'] > 0]['sku_id_x'].astype(int).astype(str)

    combine['label'] = map(lambda x, y: 1 if x > 0 and y > 0 else 0, combine['sku_id_y'], combine['sku_id_x'])
    combine['pred'] = map(lambda x, y: 1 if x == y else 0, combine['sku_id_y'], combine['sku_id_x'])
    # calculate judgement
    label_recall = recall(combine, 'label')
    label_precision = precision(combine, 'label')
    pred_recall = recall(combine, 'pred')
    pred_precision = precision(combine, 'pred')

    print "The final score is: %f" % score(label_recall, label_precision, pred_recall, pred_precision)