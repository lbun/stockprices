import bitfinex
import pandas as pd
import datetime
import time
import pickle
import datetime
from datetime import timedelta

#### names = ['time', 'open', 'close', 'high', 'low', 'volume']
t_start = datetime.datetime(2014, 1, 1, 0, 0) #starting from 1st January
t_start = time.mktime(t_start.timetuple()) * 1000
t_end = datetime.datetime(2014, 1, 2, 0, 0) #starting from 1st January
t_end = time.mktime(t_end.timetuple()) * 1000
result = api_v2.candles(symbol='btcusd', interval='1m',  limit=1000, start=t_start, end=t_end)
print(t_start,t_end)
df = pd.DataFrame(result,columns=names)

def append_and_save(dataframe):
    for i in range(5):
        try:
            dataframe = pd.read_pickle('dataframe_bitcoin')
        except:
            pass
        print(dataframe.shape)
        x = dataframe['time'].max()
        y = x + 24*60*60*1000
        result_temp = api_v2.candles(symbol='btcusd', interval='1m',  limit=1000, start=x, end=y)
        df_temp = pd.DataFrame(result_temp,columns=names)
        dataframe = dataframe.append(df_temp)
        pd.to_pickle(dataframe,'dataframe_bitcoin')
        time.sleep(2)

append_and_save(df)
