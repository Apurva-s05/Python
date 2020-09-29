
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
