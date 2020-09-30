#Hash table or hash map is type of data structure that maps keys to its value pair.

#Dictionary
emplyoee_id={'Ava':'001','Dave':'002','Joe':'003'}
print(emplyoee_id)
#op={'Ava': '001', 'Dave': '002', 'Joe': '003'}

#Nasted-Dictionary
emplyoee_details={'Employee':{'deva':{'Id':'001','Salary':'20000','Designation':'Team Lead'},
                              'Reva':{'Id':'002','Salary':'50000','Designation':'Team Manager'}}}
print(emplyoee_details)
#op={'Employee': {'deva': {'Id': '001', 'Salary': '20000', 'Designation': 'Team Lead'}, 'Reva': {'Id': '002', 'Salary': '50000', 'Designation': 'Team Manager'}}}

#Accessing
emplyoee_dict['Dave']
#op='002'

print(emplyoee_dict.keys())
#op=dict_keys(['Ava', 'Dave', 'Joe'])

print(emplyoee_dict.values())
#op=dict_values(['001', '002', '003'])

#using for loop#
#1.
for x in emplyoee_dict:
    print(x)
#op=            
Ava
Dave
Joe

#2.
for x in emplyoee_dict.values():
    print(x)
#op=
001
002
003

#3.
for x,y in emplyoee_dict.items():
    print(x,y)
#op=
Ava 001
Dave 002
Joe 003

#Updating#
emplyoee_dict['Ava']='005'
emplyoee_dict['chris']='004'
print(emplyoee_dict)
#op={'Ava': '005', 'Dave': '002', 'Joe': '003', 'ava': '005', 'chris': '004'}

#Deleting#
emplyoee_dict.pop('Ava')
#op='005'

emplyoee_dict.popitem()
#op=('chris', '004')

del emplyoee_dict['Joe']
print(emplyoee_dict)
#op={'Dave': '002', 'ava': '005'}

#Dataframe:It is a two dimentional data structure that consist of columns of various type.It is very similar to python dictionary and can coverted into pandas dataframe.

import pandas as pd
df = pd.DataFrame(emplyoee_details['Employee'])
print(df)
#op=
                  deva          Reva
Id                 001           002
Salary           20000         50000
Designation  Team Lead  Team Manager
