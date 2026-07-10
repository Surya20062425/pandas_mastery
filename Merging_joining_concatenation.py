# --- Create sample datasets ---
df_employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [1, 2, 1, 3]
})

df_departments = pd.DataFrame({
    'dept_id': [1, 2, 3, 4],
    'dept_name': ['Engineering', 'Sales', 'HR', 'Marketing'],
    'budget': [500000, 300000, 200000, 250000]
})

df_projects = pd.DataFrame({
    'emp_id': [101, 101, 102, 104],
    'project': ['Alpha', 'Beta', 'Gamma', 'Alpha'],
    'hours': [120, 80, 150, 90]
})

# --- 1. Merge (SQL-style join) ---
merged = pd.merge(
    df_employees,               # Left DataFrame
    df_departments,             # Right DataFrame
    on='dept_id',               # Column to join on (must exist in both)
    how='left'                  # Join type: 'left', 'right', 'inner', 'outer'
)

# --- 2. Merge on different column names ---
merged_diff = pd.merge(
    df_employees,
    df_projects,
    left_on='emp_id',           # Column in left DataFrame
    right_on='emp_id',          # Column in right DataFrame
    how='inner'
)

# --- 3. Concatenate (stack DataFrames vertically or horizontally) ---
df_new_hires = pd.DataFrame({
    'emp_id': [105, 106],
    'name': ['Eve', 'Frank'],
    'dept_id': [2, 1]
})

all_employees = pd.concat([df_employees, df_new_hires], axis=0, ignore_index=True)
# axis=0: stack vertically (add rows)
# axis=1: stack horizontally (add columns)
# ignore_index=True: Reset index to 0,1,2...
