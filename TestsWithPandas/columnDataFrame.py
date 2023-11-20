import pandas

data = {

    'name': 'Howard Ian Peter Jonah Kellie'.split(),

    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),

    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),

    'age' : [32, 22, 25, 29, 38]

}


dataFrame = pandas.DataFrame(data)

# Culd be dataFrame['age']
dataFrame_column = dataFrame.age 

# dataFrame_column is a Series 
print(f"type: {type(dataFrame_column)}") 

print(f"Age mean: {dataFrame_column.mean()}")

print(f"dataFrame_column: \n{dataFrame_column}")

# More the one column 
columns = ['name', 'cpfs']

dataFrame_two_column = dataFrame[columns]

# Because has to columns the dataFrame type, now, is DataFrame
print(f"dataFrame_two_columns type: {type(dataFrame_two_column)}")

print(f"dataFrame_two_column: \n{dataFrame_two_column}")



