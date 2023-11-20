import pandas 

df_selic = pandas.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

# by represents which value will be the reference to the sort function.
# ascending represents which order the values will be sorted.
# inplace is for save the sort change in the df_selic variable.
df_selic.sort_values(by='data', ascending=False, inplace=True)
print(df_selic.head())

