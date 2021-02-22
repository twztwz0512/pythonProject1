import tushare as ts
import pandas as pd
import pymysql

# d = ts.get_hist_data('600848') #一次性获取全部日k线数据
# print(d)
# data = ts.get_stock_basics()
# print(data)
ts.set_token('68572fd4a7cb1abc0981ff459ad3171cbd6d9ca134e0a2032c4558de')
pro = ts.pro_api()
#
# # 查询当前所有正常上市交易的股票列表
# data = pro.stock_basic(exchange='',
#                        list_status='L',
#                        fields='ts_code,symbol,name,area,industry,list_date')
# print(data)

# # 一次性获取2018-2020年日k线数据
# df0 = pro.daily(ts_code='600000.sh',start_date='20180101',end_date='20201231')
# print(df0)
# 通过日期获取历史某一天的全部历史
df1 = pro.daily(trade_date='20201231')
print(df1)

import datetime
import time


def getDateList(start_date, end_date):
    Searchtime = []
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    Searchtime.append(start_date.strftime('%Y-%m-%d'))
    while start_date < end_date:
        start_date += datetime.timedelta(days=1)
        Searchtime.append(start_date.strftime('%Y-%m-%d'))
    return Searchtime

Searchtime = getDateList("2018-01-01","2020-12-31")

def Catchstockdata():
    # time1 = '2018-01-01'
    while time1 in iter(Searchtime):
        df1 = pro.daily(trade_date=time1)
        print(df1)
        time.sleep(2)
        time1 = datetime.timedelta(days=1)



Catchstockdata()

# # 3s
# timer(3)
