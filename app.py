import numpy as np
import pandas as pd
from pandas_datareader import data as dt

# Calculating companies security risk

# PG - Procter & Gamble
# BEI.DE - Beiersdorf

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

# import data from yahoo finance

for t in tickers:
    sec_data[t] = dt.DataReader(t, data_source='yahoo', start='2007-01-01', end='2018-01-01')['Adj Close']

# calculating the logarithmic rate of return

sec_returns = np.log(sec_data / sec_data.shift(1))

# Plotting average rate of return

print('Annual average rate of return')

# mean() - Returns the daily average rate of return
# assuming 250 is the trading days in a year, we can get the annual average rate of return
print(sec_returns[tickers].mean() * 250)

print('Annual Risk - standard deviation')

# std() - returns standard deviation
# need to multiply with square root of 250
# because standard deviation is square root of the variance
print(sec_returns[tickers].std() * 250 ** 0.5)

