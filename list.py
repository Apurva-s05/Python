#Print list values
x=[10 , 20 , 30 , 30 , "Apple" ,"Kivi" , "Banana"]
x
#op=[10, 20, 30, 30, 'Apple', 'Kivi', 'Banana']

#Lenghh
len(x)
#op=7

#Change value at given index
x[2] = 35
#op=[10, 20, 35, 30, 'Apple', 'Kivi', 'Banana']

#position
x[2:6]
#op=[30, 30, 'Apple', 'Kivi']

x[-3]
#op='Apple'

x[5]
#op='Kivi'

#adds value at end of list
x.append(10)
x
#op=[10, 20, 35, 30, 'Apple', 'Kivi', 'Banana', 10]

#insert value at given index
x.insert(5,100)
x
#op=[10, 20, 35, 30, 'Apple', 100, 'Kivi', 'Banana', 10]

#reverse the list
x.reverse()
x
#op=[10, 'Banana', 'Kivi', 100, 'Apple', 30, 35, 20, 10]
