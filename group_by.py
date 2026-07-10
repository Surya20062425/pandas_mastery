import pandas as pd
import numpy as np
# --- Basic GroupBy ---
dept_stats = df.groupby('Department')['Salary'].mean()   # Average salary per department

# --- Multiple aggregations ---
dept_summary = df.groupby('Department').agg({
    'Salary': ['mean', 'median', 'min', 'max', 'count'],
    'Employee': 'count'
})

# --- Custom aggregation with named functions ---
def salary_range(x):
    return x.max() - x.min()

dept_custom = df.groupby('Department').agg(
    avg_salary=('Salary', 'mean'),
    total_employees=('Employee', 'count'),
    salary_spread=('Salary', salary_range)
)

# --- Transform (keep original shape, add computed columns) ---
df['Dept_Avg'] = df.groupby('Department')['Salary'].transform('mean')
df['Salary_vs_Dept_Avg'] = df['Salary'] - df['Dept_Avg']

# --- Filter groups ---
large_depts = df.groupby('Department').filter(lambda x: len(x) > 1)  # Only groups with >1 member
