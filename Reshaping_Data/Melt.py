import numpy as np
import pandas as pd

# Convert wide format to long format
wide = pd.DataFrame({
    'id': [1, 2, 3],
    'jan_sales': [100, 200, 150],
    'feb_sales': [110, 210, 160],
    'mar_sales': [120, 220, 170]
})

long = wide.melt(
    id_vars=['id'],              # Columns to keep as identifiers
    value_vars=['jan_sales', 'feb_sales', 'mar_sales'],  # Columns to unpivot
    var_name='month',            # Name for the new categorical column
    value_name='sales'           # Name for the new value column
)

