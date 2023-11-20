import pandas
from matplotlib import pyplot 


# Reading the json file
df_selic = pandas.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

# Sorting the selic values 
df_selic.sort_values(by=['data'], inplace=True)

# Creating the list of index
list_index = [f'selic_{index}' for index in df_selic.index]

# Setting the new index for each value 
df_selic.set_index(keys=[list_index], inplace=True)

date_list = df_selic['data'].to_list()
value_list = df_selic['valor'].to_list()


pyplot.plot(date_list, value_list)