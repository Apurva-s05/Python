

                                                                  #deque#
from collections import deque
a = ['p','y','t','h','o','n']
d = deque(a)
print(d)
#op=deque(['p', 'y', 't', 'h', 'o', 'n'])

d.append('python')
d
#op=deque(['p', 'y', 't', 'h', 'o', 'n', 'python'])

d.appendleft('python')
d
#op=deque(['python', 'python', 'p', 'y', 't', 'h', 'o', 'n', 'python'])
d.pop()
d
#op=deque(['python', 'python', 'p', 'y', 't', 'h', 'o', 'n'])

d.popleft()
#op=deque(['python', 'p', 'y', 't', 'h', 'o', 'n'])


                                                   
                                                               #ChainMap#
from collections import ChainMap
a = {1:'edureka',2:'python'}
b = {3:'ML',4:'AI'}
c = ChainMap(a,b)
print(c) 
 
 
                                                               #counter#
from collections import Counter
a = (1,1,2,2,2,4,5,6,7,4,2,5,8)
b = Counter(a)
print(b)
#op=Counter({2: 4, 1: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1})

                                                               #OrderedDict#
from collections import OrderedDict
d = OrderedDict()
d[1]='p'
d[2]='y'
d[3]='t'
d[4]='h'
d[5]='o'
d[6]='n'
print(d)
#op=OrderedDict([(1, 'p'), (2, 'y'), (3, 't'), (4, 'h'), (5, 'o'), (6, 'n')])


print(list(d.keys()))
#op=[1, 2, 3, 4, 5, 6]

d[1]='j'
d
#op=OrderedDict([(1, 'j'), (2, 'y'), (3, 't'), (4, 'h'), (5, 'o'), (6, 'n')])



