import nummpy as np
import pandas as pd 

# --- Create a time series ---
dates = pd.date_range(
    start='2024-01-01',         # Start date
    end='2024-12-31',           # End date
    freq='D'                    # Frequency: 'D'=daily, 'H'=hourly, 'W'=weekly, 'M'=monthly
)

ts = pd.Series(
    np.random.randn(len(dates)).cumsum() + 100,  # Cumulative random walk
    index=dates,
    name='Stock_Price'
)

# --- Time-based indexing (extremely powerful) ---
jan_data = ts['2024-01']        # Select entire January 2024
q1_data = ts['2024-01':'2024-03']  # Select Q1 (inclusive)

# --- Resampling (change frequency) ---
monthly_mean = ts.resample('M').mean()    # Downsample to month-end, take mean
weekly_sum = ts.resample('W').sum()       # Weekly totals

# --- Rolling window statistics ---
rolling_avg = ts.rolling(window=30).mean()      # 30-day moving average
exp_decay = ts.ewm(span=30).mean()            # Exponentially weighted moving average

# --- Shift and diff (for calculating returns/changes) ---
ts['lag_1'] = ts.shift(1)                     # Previous day's value
ts['daily_change'] = ts.diff(1)               # Change from previous day
ts['pct_change'] = ts.pct_change() * 100    # Percentage change
