import pandas 

list_names = 'Howard Ian Peter Jonah Kellie'.split()

list_cpf = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

list_email = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()

list_age = [32, 21, 25, 29, 38]

dataFrame = pandas.DataFrame(list_names, columns=['names'])

print(dataFrame)

dataFrame = pandas.DataFrame(list_names, columns=['names'], index=list_cpf)

print(dataFrame)

data = list(zip(list_names, list_cpf, list_age, list_email))

print(data)

dataFrame = pandas.DataFrame(data, columns=['name', 'cpfs', 'age', 'email'])

print(dataFrame)


# With dict

data = {

    'name': 'Howard Ian Peter Jonah Kellie'.split(),

    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),

    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),

    'age' : [32, 22, 25, 29, 38]

}

dataFrame = pandas.DataFrame(data)

print(dataFrame)