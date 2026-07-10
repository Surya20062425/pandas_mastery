# --- Method 1: .loc[] (Label-based indexing) ---
row_101 = df.loc[101]                    # Select row WHERE index label == 101
rows_multi = df.loc[101:103]             # Slice from label 101 to 103 (INCLUSIVE!)
alice_salary = df.loc[101, 'Salary']     # Select specific cell: row label, column name

# --- Method 2: .iloc[] (Position-based indexing) ---
first_row = df.iloc[0]                   # First row (position 0), regardless of index label
last_three = df.iloc[-3:]                # Last 3 rows using negative indexing
cell = df.iloc[0, 2]                     # Row position 0, column position 2

# --- Method 3: Boolean masking (Filter rows by conditions) ---
high_earners = df[df['Salary'] > 80000]  # Returns only rows where condition is True

# Complex boolean conditions (MUST use parentheses!)
eng_high = df[
    (df['Department'] == 'Engineering') &   # AND operator
    (df['Salary'] > 100000)
]

# String methods via .str accessor
eng_depts = df[df['Department'].str.contains('Eng')]  # Regex-capable string matching
