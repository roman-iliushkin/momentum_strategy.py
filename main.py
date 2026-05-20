import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import seaborn as sns
from matplotlib import pyplot as plt

from pandas.core.interchange.dataframe_protocol import DataFrame

tickers = ["SPY", "QQQ", "GLD", "TLT", "EEM",
           "IWM", "XLE", "XLF", "XLK", "VNQ"]

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2025, 12, 31)

data = yf.download(tickers, start, end)

monthly_prices = data["Close"].resample("ME").last()
returns = monthly_prices.pct_change(3)

top3 = returns.apply(lambda row: row.nlargest(3).index.tolist(), axis = 1)
top3 = top3.shift(1)

monthly_returns = monthly_prices.pct_change(1)

portfolio_return = {}
previous_assets = set()

for date, assets in top3.items():

    if assets is None:
        continue

    current_assets = set(assets)
    changed_assets = current_assets ^ previous_assets
    cost = 0.001 * (len(changed_assets)/3)

    portfolio_return[date] = monthly_returns.loc[date, assets].mean() - cost
    previous_assets = current_assets

portfolio_return = pd.DataFrame.from_dict(portfolio_return, orient='index')
total = (1+portfolio_return).cumprod()

all_assets_equity = (1 + monthly_returns.loc[total.index]).cumprod()

all_assets_equity["Portfolio"] = total[0]

plt.figure(figsize=(14, 7))
sns.set_theme(style="whitegrid")

sns.lineplot(data=all_assets_equity.drop(columns=['Portfolio']), palette="tab20", alpha=0.6)

plt.plot(all_assets_equity.index, all_assets_equity['Portfolio'], color='crimson', linewidth=4, label='Our Portfolio')

plt.yscale('log')
plt.title('Comparison (2010-2025)', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Capital growth')

plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()

plt.show()
