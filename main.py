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

tickers = ["TSLA", "AAPL", "NVDA", "GOOGL", "AMZN", "NFLX"]
tickers.sort()

data = {}

#get all stock info
for ticker in tickers:
    stock = yf.Ticker(ticker)
    data[ticker] = {'ticker': ticker,
                    'dayHigh': stock.info['dayHigh'],
                    'dayLow': stock.info['dayLow'],
                    'close': stock.info['previousClose'],
                    'marketCap': stock.info['marketCap']}
    #print(f"Ticker: {ticker} \nDailey High: {stock.info['dayHigh']} \nDailey Low: {stock.info['dayLow']} \nMarket Cap: {stock.info['marketCap']}")
#pprint.pprint(msft.info)

#get historical market data
#hist = aapl.history(period="10d")

pprint.pprint(data)




