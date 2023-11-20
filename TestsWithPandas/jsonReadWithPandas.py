import pandas

# Reading json file
# url: https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json 
df_selic = pandas.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

# Printing the df_selic information 
print(df_selic.info())
print(df_selic)

# Removing duplicates(drop_duplicates) lines and keeping the last register (keep='last')
# With the parameter inplace=True we are salveing the change in the DataFrame

df_selic.drop_duplicates(keep='last', inplace=True)

print(df_selic)
 