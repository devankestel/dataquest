## 1. Reading CSV Files with Encodings ##

import pandas as pd

laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
laptops.info()

## 2. Cleaning Column Names ##

new_columns = []

for column in laptops.columns: 
    new_columns.append(column.strip())
    
laptops.columns = new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean_col(col):
    clean_col = (col
                 .strip()
                 .lower()
                 .replace(')','')
                 .replace('(','')
                 .replace('operating system', 'os')
                 .replace(' ', '_'))
    return clean_col

new_columns = []
for column in laptops.columns:
    new_columns.append(clean_col(column))
    
laptops.columns = new_columns
    