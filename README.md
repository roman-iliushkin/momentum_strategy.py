# Multi-Asset Momentum Strategy

A momentum-based portfolio rotation strategy that dynamically 
selects the top-3 performing ETFs from a universe of 10 assets, 
rebalanced monthly with transaction costs.

## Strategy Logic
1. Universe: 10 liquid ETFs across asset classes
2. Signal: 3-month trailing return for each asset
3. Selection: Top-3 assets by momentum score
4. Execution: Equal-weight portfolio, rebalanced monthly
5. Costs: 0.1% transaction cost per asset change
6. Leakage control: signals based on t-1 month data

## Asset Universe
| Ticker |    Asset Class   |
|--------|------------------|
|   SPY  | US Large Cap     |
|   QQQ  | US Technology    |
|   GLD  | Gold             |
|   TLT  | Long-Term Bonds  |
|   EEM  | Emerging Markets |
|   IWM  | US Small Cap     |
|   XLE  | Energy           |
|   XLF  | Financials       |
|   XLK  | Technology       |
|   VNQ  | Real Estate      |

## Results (2010–2025)
|           Asset        | Total Return |
|------------------------|--------------|
| XLK (Tech)             |     17.19x   |
| QQQ (Nasdaq)           |     16.66x   |
| XLF (Finance)          |     6.36x    |
| SPY (S&P 500)          |     8.53x    |
| **Momentum Portfolio** |   **8.06x**  |
| VNQ (Real Estate)      |     3.95x    |
| GLD (Gold)             |     3.76x    |
| XLE (Energy)           |     2.79x    |
| EEM (Emerging)         |     2.02x    |
| TLT (Bonds)            |     1.51x    |

## Key Findings
- Portfolio outperformed 6 out of 10 individual assets
- Underperformed vs XLK and QQQ which dominated 2010–2025
- In hindsight, 100% QQQ was optimal — but momentum 
  provided diversified exposure without knowing the future winner
- Transaction costs reduce returns but reflect real trading conditions
- Momentum effect is real but modest in a sustained bull market

## Limitations
- Backtest covers a strong bull market — results may differ 
  in bear or sideways markets
- No slippage model beyond flat transaction cost
- Monthly rebalancing may miss intra-month momentum shifts
- Small universe of 10 assets limits diversification

## Tech Stack
Python · pandas · NumPy · yfinance · matplotlib · seaborn

## How to Run
git clone https://github.com/roman-iliushkin/momentum-strategy
cd momentum-strategy
pip install -r requirements.txt
python main.py

## Next Steps
- [ ] Add Sharpe ratio and max drawdown metrics
- [ ] Test on different time periods (2000–2010, bear market)
- [ ] Extend universe to 50+ assets
- [ ] Add walk-forward validation
