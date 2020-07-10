from math import isnan
from pandas import Series, DataFrame
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt
%matplotlib inline

def read_data(ticker_list, start=dt.datetime(2019, 1, 2), end=dt.datetime(2019, 12, 31)):
    """
    This function reads in closing price data from Yahoo
    for each tick in the ticker_list.
    """
    ticker = DataFrame()

    for tick in ticker_list:
        prices = data.DataReader(tick, 'yahoo', start, end)
        closing_prices = prices['Close']
        ticker[tick] = closing_prices

    return ticker

def returns(index, start=1970, end=2021):
    """Calculate returns of a particular index and store them in dictionary mapping.  Index's name
       must be consistent with a corresponding name on Yahoo."""
    assert start >= 1970, 'start < 1970 (Unix epoch time) cause mktime error for some computers'
    temp = dict()
    p1, p2 = None, None
    for year in range(start, end):
        for i in indices_data.loc[str(year), index]: #Look for stock value that is not NaN from above
            if not isnan(i):
                p1 = i
                break #When the first number is not NaN, record that number and break this loop
            
        for i in range(len(indices_data.loc[str(year), index])): #Look for stock value that is not NaN from below
            if not isnan(indices_data.loc[str(year), index][-(1+i)]): #From the last value: start with -1
                p2 = indices_data.loc[str(year), index][-(1+i)]
                break
        try:
            temp[str(year)] = (p2-p1)/p1
        except: #p1 = None or p2 = None, i.e., when all entries in a particular year are NaN
            pass
    return temp #Note that temp is dict.

indices_list = {'^GSPC': 'S&P 500', '^IXIC': 'NASDAQ','^DJI': 'Dow Jones', '^N225': 'Nikkei'}
indices_data = read_data(indices_list, start=dt.datetime(1970, 1, 2),end=dt.datetime(2020, 12, 31))
plot_map = {(0,0):'^GSPC', (0, 1): '^IXIC', (1,0):'^DJI', (1, 1):'^N225' } #Suppose I don't know ".flatten".
fig, axes = plt.subplots(2, 2, figsize= (10, 6))  #following how to do multiple plots from previous
for i in plot_map:
    y = Series(returns(plot_map[i]))
    y.index = y.index.astype('int64') #if you don't do this your x-axis will be unreadable.
    axes[i[0],i[1]].plot(y)
    axes[i[0],i[1]].set_ylabel('Percentage Change', fontsize=12)
    axes[i[0],i[1]].set_title(indices_list[plot_map[i]])
plt.tight_layout() #if plt.show() is used instead of plt.tight_layout, figures will be cramped a bit.




        

    
        
    
    

    

    
