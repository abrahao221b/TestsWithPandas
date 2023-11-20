import pandas 

# Site: https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/38092-ipca-foi-de-0-26-em-setembro
url = 'https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/38092-ipca-foi-de-0-26-em-setembro'

list_dfs = pandas.read_html(url)

print(f"type(list_dfs): {type(list_dfs)}")

print(f"Lenght of list_dfs: {len(list_dfs)}")

# Tables contents

# National Consumer Price Index Broad variation table by period
df_period =  list_dfs[0]

print(f"df_period.shape: {df_period.shape}")

print(f"df_period.dtypes: {df_period.dtypes}")

print("Printing the df_period.head(): \n\n")
print(df_period.head())