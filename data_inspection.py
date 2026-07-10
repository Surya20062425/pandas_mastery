# --- Essential First Commands (run these on ANY new dataset) ---

# 1. Shape and structure
print(df.shape)           # (rows, columns) → (4, 4)
print(df.columns)         # Index object of column names
print(df.index)           # Index object of row labels
print(df.dtypes)          # Data type of EACH column (crucial for debugging)

# 2. Content preview
print(df.head(3))         # First 3 rows (default is 5)
print(df.tail(2))         # Last 2 rows
print(df.sample(2))       # Random 2 rows (useful for spotting data quality issues)

# 3. Statistical summary
print(df.describe())      # Count, mean, std, min, 25%, 50%, 75%, max for numeric cols
print(df.describe(include='all'))  # Include categorical columns too

# 4. Memory and metadata
print(df.info())          # Column types, non-null counts, memory usage
print(df.memory_usage(deep=True))  # Deep=True counts object column memory accurately
