import pandas as pd
import numpy as np
#df_rows is the variable we are using to store the data_frame details
df_rows = pd.DataFrame([
    {'Employee': 'Alice', 'Salary': 95000},      # Each dict = one row
    {'Employee': 'Bob', 'Salary': 72000},
    {'Employee': 'Charlie', 'Salary': 110000},
    {'Employee':'kiran','salary':44},
    {'Conistable':'samay','salary':22},#conistble
    {'Ethical_hacker':'nishanth','salary':3333},#Ethical Hacker 
    {'marketing_manager':'naveen','salary':4444},#Marketing manager
    {'rowdy-sheeter':'pavan','salary':500000000},#Rowdy-sheeter
    {'Boxer':'sathvik','salary':400},#Boxer
    {'Doctor':'srikumar','salary':200},#Doctor
    {'Electrician':'ashish','salary':4},#elctrician
    {'Esport-player':'kalyan','salary':2},#Esport Player
])
#in above case we used the method that mimics the dictionarie
#each dictionary is equal to the new row 

print(df_rows)