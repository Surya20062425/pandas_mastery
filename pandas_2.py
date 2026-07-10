import pandas as pd
import numpy as np
#pd.Dataframe is used to show the data in a format 
#we are using the titles Employee , Department , Salary ,Start_Date 
#Employee , Department , Salary ,Start_Date  pocess the data 

df=pd.DataFrame(data={   'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Department': ['Engineering', 'Sales', 'Engineering', 'HR'],
        'Salary': [95000, 72000, 110000, 68000],
        'Start_Date': pd.to_datetime(['2020-03-15', '2019-07-01', '2021-01-10', '2018-11-20'])}
#pd.to_datetime it usually used to setup the date and time of the  data_frame
    
,index=[21,23,32,43])
print(df)#PRINTING THE DATA STORED IN PD VARIABLE 
#Line-by-line breakdown: - pd.DataFrame(...): Constructor. Creates a 2D tabular structure. - data={...}: Dict of column_name → array-like. Each array must be the same length (4 elements). - 'Start_Date': pd.to_datetime(...): Critical best practice. Never store dates as strings. pd.to_datetime() parses strings into datetime64[ns] objects, enabling time-series operations.