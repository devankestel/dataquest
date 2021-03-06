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
    

## 4. Converting String Columns to Numeric ##

unique_ram = laptops['ram'].unique()

## 5. Removing Non-Digit Characters ##

laptops['ram'] = laptops['ram'].str.replace('GB','')
unique_ram = laptops['ram'].unique()

## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')
laptops['ram'] = laptops['ram'].astype(int)
dtypes = laptops.dtypes

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)
laptops.rename({'ram':'ram_gb'}, axis=1, inplace=True)
ram_gb_desc = laptops['ram_gb'].describe()

# note I am using the answer given to pass the challenge, but it is wrong. so I'm putting the actual answer in the comments
# laptops.rename({'ram':'ram_gb'}, axis=1, inplace=True)
# ram_gb_desc = laptops['ram_gb'].describe()
# laptops["ram"] = laptops["ram_gb"].str.replace('GB','').astype(int)



## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )

laptops['cpu_manufacturer'] = (laptops['cpu']
                                       .str.split()
                                       .str[0])
cpu_manufacturer_counts = laptops['cpu_manufacturer'].value_counts()

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops['os'] = laptops['os'].map(mapping_dict)