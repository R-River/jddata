# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:02:30 2017

@author: Administrator
"""
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

if __name__ == '__main__':

    product = load_data('F:\\jdData\\JData_Product.csv')
    ax = plt.subplot(111, projection='3d')
    num_cluster = 4
    kmeans = KMeans(num_cluster).fit(product[['attr1', 'attr2', 'attr3']])
    cluster_label = kmeans.predict(product[['attr1', 'attr2', 'attr3']])
    product['cluster_label'] = cluster_label

    for i in range(num_cluster):
        locals()['c'+str(i)] = product[product['cluster_label']==i]

    colors = ['r', 'b', 'y', 'g']
    for i, c in zip(range(num_cluster), colors):
        ax.scatter(locals()['c'+str(i)]['attr1'], locals()['c'+str(i)]['attr2'], locals()['c'+str(i)]['attr3'],
                   s=50, c=c, marker='o')

    ax.set_xlabel("attr1")
    ax.set_ylabel("attr2")
    ax.set_zlabel("attr3")
    plt.show()