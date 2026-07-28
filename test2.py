import pandas as pd

df = pd.read_csv(r"C:\path\to\monthly_file.csv")
lt_ref = pd.read_csv(r"C:\path\to\aggregate_lookup.csv")

# Filter to respective month. e.g. July
df_month = df[df['Month'] == 'Jul'].copy()

# Static columns (change quarter and fiscal year respectively)
df_month['Quarter'] = 'Q3'
df_month['DAA Average'] = 34
df_month['Fiscal_Yr'] = 'FY26'

# Single merge for all lookup columns
lookup = lt_ref.drop_duplicates(subset='Supplier Name')
df_month = df_month.merge(
lookup[['Supplier Name', 'SSM', 'Category', 'FY24 Category AVG', 'SSM Target']],
on='Supplier Name',
how='left'
)

for col in ['SSM', 'Category', 'FY24 Category AVG', 'SSM Target']:
    df_month[col] = df_month[col].fillna("")

# Union with the aggregate file
union_all_df = pd.concat([df_month, lt_ref], ignore_index=True)

union_all_df

