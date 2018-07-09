# -*- coding: utf-8 -*-
# @Time    : 2018/6/4
# @Author  : ErichLee ErichLee@qq.com
# @File    : date_check_util.py
# @Comment : 日期类检查工具
#
import datetime
import time


# (1)字符串转datetime：
# def strToDate(dateStr):
#     string = '2014-01-08 11:59:58'
#     time1 = datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
#     print time1

# (2)datetime转字符串：
# def DateToStr():
#     time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
#     print time1_str

#
# now_time = datetime.datetime.now()
# timeStr = datetime.datetime.strftime(now_time,'%Y-%m-%d')
# print timeStr

def currDateFormateA():
    now_time = datetime.datetime.now()
    timeStr = datetime.datetime.strftime(now_time, '%Y-%m-%d')
    timeDate = datetime.datetime.strptime(timeStr, '%Y-%m-%d')
    return timeDate


def currDateFormate():
    now_time = datetime.datetime.now()
    return now_time


def curr_data_ymdhm():
    return str(time.strftime("%Y%m%d%H%M", time.localtime()))


def curr_date_format():
    now_time = datetime.datetime.now()
    return now_time


def curr_date_str():
    return time.strftime("%Y-%m-%d", time.localtime())


def curr_date_str2():
    return time.strftime("%Y%m%d", time.localtime())
