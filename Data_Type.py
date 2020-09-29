
                                                                                  #numbers#

x=10
print(x)  #output = 10

y=10.102
print(y)  #output = 10.102

z=25j
print(z)   #output = 25j

print(type(10))    #output = <class 'int'>


print(type(10.071))    #output = <class 'float'>

print(type(True))       #output = <class 'bool'>

print(type(5j))         #output = <class 'complex'>



                                                                                  #dictionary#
  #Unordered,can be change and no duplicate entries present.

#Print list values
x={'reptiles' : 'snakes',
    'mammals' : 'whale',
     'amphibians' : 'frog'
  }
x
#op={'reptiles': 'snakes', 'mammals': 'whale', 'amphibians': 'frog'}

#print required dictionary
x['mammals']
#op='whale'

#change value
x['amphibians'] = 'Salamanders'
#op={'reptiles': 'snakes', 'mammals': 'whale', 'amphibians': 'Salamanders'}

#print required value
x.get('reptiles')
#op='snakes'

#add value
x['birds'] = 'parrot'
x
#op={'reptiles': 'snakes',
 'mammals': 'whale',
 'amphibians': 'Salamanders',
 'birds': 'parrot'}
  
  
                                                                                   #string#


#print string
x="python"
print(x)
#op=python

#print length of string
len(x)
#op=6

#addition of two string
y=" Jupyter"
print(x+y)
#op=python Jupyter

#Upper case
x.upper()
#op='PYTHON'

#lower case
x.lower()
#op='python'

#position
x[2:6]
#op='thon'


x[-2]
#op='o'

x[5]
#op='n'






                                                                                     #List#
#Unordered,no duplicate entries present

list={"lion","king","monkey",10,10,20}
list
#op={10, 20, 'king', 'lion', 'monkey'}

range(11)
#op=range(0, 11)

set(range(11))
#op={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

a = 1,2,3
b = 4,5,6
c = [a,b]
c
#op=[(1, 2, 3), (4, 5, 6)]
