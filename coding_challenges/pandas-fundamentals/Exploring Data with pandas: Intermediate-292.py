## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()

## 2. Reading CSV files with pandas ##

f500 = pandas.read_csv('f500.csv')
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0, 0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500[0:3]
first_seventh_row_slice = f500.iloc[[0,6], 0:5]

## 5. Using pandas methods to create boolean masks ##

previous_rank_is_null_series = f500["previous_rank"].isnull()
previous_rank_null_df = f500[previous_rank_is_null_series]
null_previous_rank = previous_rank_null_df[["company", "rank", "previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank[0:5]

## 7. Pandas Index Alignment ##

previously_ranked_is_not_null_series = f500['previous_rank'].notnull() 
previously_ranked = f500[previously_ranked_is_not_null_series]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
f500['rank_change'] = rank_change

## 8. Using Boolean Operators ##

large_revenue = f500['revenues'] > 100000
negative_profits = f500['profits'] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500[combined]

## 9. Using Boolean Operators Continued ##

brazil_venezuela_series = (f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')

brazil_venezuela = f500[brazil_venezuela_series]
tech_not_usa = ~(f500['country'] == 'USA') & (f500['sector'] == 'Technology')
tech_not_usa_df = f500[tech_not_usa]
tech_outside_usa = tech_not_usa_df.head(5)

## 10. Sorting Values ##

hq_in_japan = f500[f500['country'] == 'Japan']
sorted_rows = hq_in_japan.sort_values('employees', ascending=False)
first_row = sorted_rows.iloc[0]
top_japanese_employer = first_row['company']

## 11. Using Loops with pandas ##

top_employer_by_country = {}
unique_countries = f500['country'].unique()

for country in unique_countries:
    selected_rows = f500[f500['country'] == country]
    sorted_rows = selected_rows.sort_values('employees', ascending=False)
    first_row = sorted_rows.iloc[0]
    company_name = first_row['company']
    top_employer_by_country[country] = company_name

## 12. Challenge: Calculating Return on Assets by Country ##

f500['roa'] = f500['profits']/f500['assets']
top_roa_by_sector = {}
sectors = f500['sector'].unique()

for sector in sectors:
    selected_rows = f500[f500['sector'] == sector]
    sorted_rows = selected_rows.sort_values('roa', ascending=False)
    first_row = sorted_rows.iloc[0]
    company_name = first_row['company']
    top_roa_by_sector[sector] = company_name