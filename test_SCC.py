__author__ = 'ardila'
from SCC import kosaraju

f ="""1 4
4 3
3 1
4 6
6 7
6 10
10 11
11 10
7 6
2 5
5 2
5 7
5 8
8 9
7 11"""

print f
kosaraju(f.split('\n'))

