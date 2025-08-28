import yfinance as yf 
import numpy as np 
import pandas as pd 
import pandas_datareader as data 
from pandas_datareader import data, wb 

# checks if its an object like

stickers = ['GOOG', 'AAPL', 'AMZN', 'META', 'MSFT', 'GSPC'] 
table = [] 
stick_dict = {} 

# GSPC --> Stock of S&P 500 
# AAPL --> Apple 
# META --> Facebook
# AMZN --> Amazon 
# MSFT --> Microsoft 



GOOG = yf.download('GOOG', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)
print(GOOG)

AAPL = yf.download('AAPL', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)

META = yf.download('META', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)

AMZN = yf.download('AMZN', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)


GSPC = yf.download('GSPC', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)


MSFT = yf.download('MSFT', start="2012-05-18", end="2023-01-01", group_by="ticker", auto_adjust=False)


list1 = [GOOG, AAPL, META, AMZN, GSPC, MSFT] 

# Exploratory Data Analaysis (EDA)


print(GOOG.isnull().sum())


dataset = pd.concat([GOOG.Close, AAPL.Close, 
                     META.Close, AMZN.Close, 
                     MSFT.Close, 
                     GSPC.Close], axis=1)


print(dataset) 

