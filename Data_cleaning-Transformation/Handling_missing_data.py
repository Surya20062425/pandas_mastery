# Create data with intentional missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['x', 'y', 'z', 'w']
})

# --- Detect missing values ---
print(df_missing.isna())          # Boolean DataFrame: True where value is NaN
print(df_missing.isna().sum())    # Count NaNs per column (essential data quality check)

# --- Drop missing values ---
df_dropped = df_missing.dropna()              # Drop ANY row with at least one NaN
df_drop_cols = df_missing.dropna(axis=1)      # Drop COLUMNS with any NaN
df_thresh = df_missing.dropna(thresh=2)       # Keep rows with at least 2 non-NaN values

# --- Fill missing values ---
df_filled = df_missing.fillna(0)              # Fill with scalar
df_filled = df_missing.fillna({'A': 0, 'B': 99})  # Column-specific fill values

# Forward fill (propagate last valid value forward) and backward fill
df_ffill = df_missing.fillna(method='ffill')  # Use last valid observation
df_bfill = df_missing.fillna(method='bfill')  # Use next valid observation

# Fill with statistical measures
df_filled = df_missing.copy()
df_filled['A'] = df_filled['A'].fillna(df_filled['A'].mean())  # Mean imputation
