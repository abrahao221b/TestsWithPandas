import pandas

data = {

    'name': 'Howard Ian Peter Jonah Kellie'.split(),

    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),

    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),

    'age' : [32, 22, 25, 29, 38]

}

df_data = pandas.DataFrame(data)

print("Test with DataFrame")

print(df_data.info()) # Information about the DataFrame 

print(f"How manu lines and columns: {df_data.shape}")

print(f"Data types: {df_data.dtypes}")

print(f"Min value: {df_data.min()}")

print(f"Max value: {df_data.max()}")

print(f"Mean: {df_data.mean()}")

print(f"Standard deviation: {df_data.std()}")

print(f"Median: {df_data.median()}")

print(f"Describe: {df_data.describe}")

df_data.head()

