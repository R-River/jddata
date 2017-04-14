# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:50:45 2017

@author: Administrator
"""

import pandas as pd
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
sys.path.append('F:\jdData')

def load_data(file_name):
    """read files"""
    with open(file_name) as f:
        head = f.readline().strip().strip('\xef\xbb\xbf').split(',')
        pass

    tb = pd.read_table(file_name, sep=',')
    tb = tb.rename(columns={tb.columns[0]: head[0]})

    return tb

def change_age_to_flag(record):
    """change age column in user file to flag"""
    if record == "-1":
        return 0
    elif record == "15岁以下":
        return 1
    elif record == "16-25岁":
        return 2
    elif record == "26-35岁":
        return 3
    elif record == "36-45岁":
        return 4
    elif record == "46-55岁":
        return 5
    elif record == "56岁以上":
        return 6
    else:
        return -1


if __name__ == '__main__':
    
    user=load_data('F:\jdData\JData_User.csv')
    user['age']=map(change_age_to_flag,user['age'])