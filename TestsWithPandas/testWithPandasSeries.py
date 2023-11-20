import pandas 

series_data = pandas.Series([10.2, -1, None, 15, 23.4])

print(f'Quantity of lines: {series_data.shape}')
print(f'Data types: {series_data.dtype}')
print(f'Unique values? {series_data.is_unique}')
print(f'Has nans values? {series_data.hasnans}')
print(f'How many values? {series_data.count()}')
print(f'Min value: {series_data.min()}')
print(f'Max value: {series_data.max()}')
print(f'Mean: {series_data.mean()}')
print(f'Standard deviation: {series_data.std()}')
print(f'Median: {series_data.median()}')
print(f'Descibe: \n{series_data.describe()}')
print(series_data)