import pandas as pd 
import numpy as np

array_data = np.random.randn(1000, 5)     #array_data is an variable 
#np.random.randn it create the random rows
#np.random.randn(rowa,,cols) we describe that how many rows and columns are to be created
# 1000 rows, 5 columns of random normals
df_numpy = pd.DataFrame(
    array_data,
    columns=['A', 'B', 'C', 'D', 'E'],
    index=pd.RangeIndex(1000, name='row_id') 
          # Explicit RangeIndex
)
print(df_numpy)