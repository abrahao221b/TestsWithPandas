import pandas


df_selic = pandas.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")


df_selic.sort_values(by='data', ascending=False, inplace=True)

list_index = [f'selic_{index}' for index in df_selic.index]

df_selic.set_index(keys=[list_index], inplace=True)

# Filter with Booleans

test = df_selic['valor'] < 0.01

# print(f'test: {test}')

# Test with date

# test2 = df_selic['data'] >= pandas.to_datetime('2020-01-01')

# print(f'test2: {test2}')

# Test with logical operators

# And operator &
test3 = (df_selic['valor'] > 0.01) & (df_selic['valor'] <= 0.05)

# print(f'test3: {test3}')

# Or operator |
test4 = (df_selic['valor'] > 0.01) | (df_selic['valor'] <= 0.05)

print(f'test4: {test4}')