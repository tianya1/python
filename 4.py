#数据结构

#list
count()
insert()
append()
index()
remove()
reverse()
sort()

#stack
append()
pop()

#queue
from collections import deque
append()
popleft()

#推导式
vec = [2, 4, 6]
[3*x for x in vec]
[[x, x**2] for x in vec]
[weapon.strip() for weapon in freshfruit]
[3*x for x in vec if x > 3]
[x*y for x in vec1 for y in vec2]
 [vec1[i]*vec2[i] for i in range(len(vec1))]
 [str(round(355/113, i)) for i in range(1, 6)]   ['3.1', '3.14', '3.142', '3.1416', '3.14159']


 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


del()
a = {x for x in 'abracadabra' if x not in 'abc'}
set()


tel = {'jack': 4098, 'sape': 4139}
list(tel.keys())
sorted(tel.keys())

 {x: x**2 for x in (2, 4, 6)}


 dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}


for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
0 tic
1 tac
2 toe


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.


for i in reversed(range(1, 10, 2)):
 print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

