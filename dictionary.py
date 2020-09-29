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
