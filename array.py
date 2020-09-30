
                                                                   #Array Declaration#
#Type 1: Python Array module
import array
a=array.array('i',[1,2,3,4,5])          #fisrt array is=module name and second array is=array constructor
a
#op=array('i', [1, 2, 3, 4, 5])

#Type 2
import array as arr
a=arr.array('i',[1,2,3,4,5])
a
#op=array('i', [1, 2, 3, 4, 5])

#Type 3
from array import *
a=arr.array('i',[1,2,3,4,5])
a
#op=array('i', [1, 2, 3, 4, 5])

                                                                    #Accessing array element#
                                                                    
a[2]
#op=3

                                                                     #Array Operations#
#1.Finding length of array
len(a)
#op=6

#2.Adding elements to array
 
#I.append=When we want add element at the end of array
a.append(4000)
a
#op=array('i', [1, 2, 100, 3, 4, 5, 1000, 2000, 3000, 4000])

#II.Insert=When we want to add element at specific position
a.insert(2,100)
a
#op=array('i', [1, 2, 100, 3, 4, 5])

#III.extend=When we want to add more than one element at the end of array
a.extend([1000,2000,3000])
a
#op=array('i', [1, 2, 100, 3, 4, 5, 1000, 2000, 3000, 4000])


#3.Remove elements from array

#I.pop=Remove element and return it
#Removes last element
a.pop()
a
#op=array('i', [1, 2, 3, 4, 5, 1000, 2000, 3000])

#Remove elemnt with index value
a.pop(2)
a
#op=array('i', [1, 2, 4, 5, 1000, 2000, 3000])

#II.Remove element with specific value without returning it
a.remove(3000)
a
#op=array('i', [1, 2, 3, 4, 5, 1000, 2000])


#4.array concatination(Addition of two array)
import array as arr
a=arr.array('d',[1.1,1.2,1.3,1.4,1.5])
b=arr.array('d',[1.6,1.7,1.8,1.9,2.0])
c=a+b
c
#op=array('d', [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])

#5.Slicing an array==Array sliced using : symbol which returns range of elements that we have specified by index number
import array as arr
a=arr.array('d',[1.1,1.2,1.3,1.4,1.5])
print(a[0:3])
#op=array('d', [1.1, 1.2, 1.3])

import array as arr
a=arr.array('d',[1.1,1.2,1.3,1.4,1.5])
print(a[0:-4])
#op=array('d', [1.1])

#reverse the array
import array as arr
a=arr.array('d',[1.1,1.2,1.3,1.4,1.5])
print(a[::-1])
#op=array('d', [1.5, 1.4, 1.3, 1.2, 1.1])

#5.Looping

#I.For=Iterets over the item of array specified number of times
#1.
import array as arr
a=arr.array('i',[1,2,3,4,5,6,7])
temp=0
while temp<a[5]:
    print(a[temp])
    temp = temp + 1
#op=
1
2
3
4
5
6

#2.
x=0
while x<len(a):
      print(a[x])
      x = x +1
 #op=
1
2
3
4
5
6
7

#II.While=Iterets over the item of array until certain condition met

#for loop with slicing
#1.
import array as arr
a=arr.array('i',[1,2,3,4,5,6,7])
for x in a:
    print(x)
#op=
1
2
3
4
5
6
7

#2.
for x in a[0:3]:
        print(x)
#op=
1
2
3
