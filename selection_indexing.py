import pandas as pd
import numpy as np
df=pd.DataFrame(data={   'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Department': ['Engineering','Sales', 'Engineering', 'HR'],
        'Salary': [95000, 72000, 110000, 68000],
        'Start_Date': pd.to_datetime(['2020-03-15', '2019-07-01', '2021-01-10', '2018-11-20'])}
#pd.to_datetime it usually used to setup the date and time of the  data_frame
    
,index=[21,23,32,43])
# --- Selecting a single column (returns a Series) ---
dept = df['Department']           # Dictionary-style access
dept = df.Department              # Attribute-style (avoid if column has spaces/special chars)

# --- Selecting multiple columns (returns a DataFrame) ---
subset = df[['Employee', 'Salary']]   # DOUBLE BRACKETS required! Inner list = column names

# --- Advanced column selection by dtype ---
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
string_cols = df.select_dtypes(include=['object']).columns
