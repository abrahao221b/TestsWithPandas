import pandas 

df_selic = pandas.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

# Sorting the values
df_selic.sort_values(by='data', ascending=False, inplace=True)

# Reseting DataFrame indexes 
df_selic.reset_index(drop=True, inplace=True)

list_index = [f'selic_{index}' for index in df_selic.index]

# Function set_index, the list_value has to be put inside the []
df_selic.set_index(keys=[list_index], inplace=True)

# Min index value
print(f"Index of the min value: {df_selic['valor'].idxmin()}")

# Max index value
print(f"Index of the max value: {df_selic['valor'].idxmax()}")

# Loc method 

# One specific value
print(df_selic.loc['selic_1'])

# More the one value
# print(df_selic.loc['selic_1', 'selic_2', 'selic_3', 'selic_4', 'selic_5'])
print(df_selic.loc[:'selic_5'])

# Two arguments, rows and columns
print(df_selic.loc[['selic_0', 'selic_4', 'selic_200']]['valor'])

print(df_selic.loc[['selic_0', 'selic_10', 'selic_300']][['valor', 'data']])


# iloc method

# The method iloc uses an integer as a parameter
print(df_selic.iloc[:5])

