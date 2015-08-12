#!/usr/bin/env python2

squares = [x**2 for x in range(10)]
print(squares)

list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list)

from math import pi
list = [str(round(pi, i)) for i in range(1, 6)]
print(list)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)

#To samo co:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

#I to samo co:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

#Usuwanie del'em
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print('del a[2:4]')
print(a)

del a[:]
print('del a[:]')
print(a)

del a
print(a)
