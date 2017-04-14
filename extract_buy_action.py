# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:05:28 2017

@author: Administrator
"""

import numpy as np
import pandas as pd
from collections import Counter
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
sys.path.append('F:\jdData')

def load_data(file_name):
    """read files"""
    content=[]
    with open(file_name) as f:
        for line in f:
            content.append(line.strip()) 

    return content

def extract_wanted(in_array,cols=4):
    """extract lines with action==4"""
    idx=np.where(in_array[:,cols]=='4')
    return in_array[:][idx]

def extract_first_time(in_array):
    """take first time one user met one product"""
    
def split_list(in_list,i_num,num=100):
    """split big list and turn to array"""
    n=len(in_list)
    d=n/num

    if i_num == num-1:
#        tmp = extract_wanted(np.array(map(lambda x: x.split(','),in_list[i_num*d:])))
        tmp = np.array(map(lambda x: x.split(','),in_list[i_num*d:]))
    else:
#        tmp = extract_wanted(np.array(map(lambda x: x.split(','),in_list[i_num*d:(i_num+1)*d])))
        tmp = np.array(map(lambda x: x.split(','),in_list[i_num*d:(i_num+1)*d]))
    return tmp

def combine_splitted_array(input_list):
    """join all separated arrays into one"""
    num=100
    cols = input_list[0].split(',')
    input_list = input_list[1:]
    return_array=np.array([])
    for i in range(num):
        if i == 0:
            return_array = split_list(input_list,i,num)
        else:
            tmp = split_list(input_list,i,num)
            return_array=np.concatenate((return_array,tmp))
        print i
    re_df = pd.DataFrame(return_array,columns=cols)

    return re_df

def target_cate_and_date_format(in_df):
    """select target cate=8 and cut date into YYYY-MM-DD"""
    re_df=in_df[in_df['cate']=='8']
    re_df['date']=map(lambda x:x[:10],re_df['time'])
    
    return re_df

if __name__ == "__main__":
    
    ac2=load_data('./JData_Action_201602.csv')
#    ac2_buy=combine_splitted_array(action2)
#    ac2_buy8=target_cate_and_date_format(ac2_buy)
    
#    ac3=load_data('./JData_Action_201603.csv')
#    ac3_buy=combine_splitted_array(action3)
#    ac3_buy8=target_cate_and_date_format(ac3_buy)
   
#    ac3x=load_data('./JData_Action_201603_extra.csv')
#    ac3x_buy=combine_splitted_array(action3x)
#    ac3x_buy8=target_cate_and_date_format(ac3x_buy)

#    ac4=load_data('./JData_Action_201604.csv')
#    ac4_buy=combine_splitted_array(action4)
#    ac4_buy8=target_cate_and_date_format(ac4_buy)