'''
INF601 - Programming in Python
Assignment - Mini Project 1
I, Dawsyn Birtell, affirm that the work submitted for this assignment is entirely my own. 
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. 
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

import yfinance as yf
import pprint
import numpy as np
import matplotlib.pyplot as plt

tickers = ["TSLA", "AAPL", "NVDA", "GOOGL", "AMZN", "NFLX"]

data = {}


#get all stock info
for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")
    last10Days = []
    for date in hist['Close'][:11]:
        last10Days.append(date)
    if(len(last10Days) == 10):
        max_price = np.max(last10Days) + (np.max(last10Days) * 0.05)
        min_price = np.min(last10Days) - (np.min(last10Days) * 0.05)
        arr = np.array(last10Days)
        plt.plot(arr)
        plt.xlabel('Days Ago')
        plt.axis([1,10,min_price,max_price])
        plt.ylabel('Closing Price')
        plt.title(f'{ticker} - Last 10 Days')
        plt.savefig(f'charts//{ticker}.png')
    else:
        print(f"Error: Could not get 10 days of data. Only have {len(last10Days)} days.")



"""     data[ticker] = {'ticker': ticker,
                    'dayHigh': stock.info['dayHigh'],
                    'dayLow': stock.info['dayLow'],
                    'close': stock.info['previousClose'],
                    'marketCap': stock.info['marketCap']} """



