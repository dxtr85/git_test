#!/usr/bin/env python2

#Ta funkcja zwraca inna funkcje, z predefiniowana wartoscia dodawana
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)#f to jest funkcja lambda n=42 a x to jej argument
print(f(0))

print(f(1))

#Przekazywanie małej funkcji jako argument do innej funkcji:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
print(a)
a.append(333)
print('a.append(333)')
print(a)

a.index(333)

a.remove(333)
print('a.remove(333)')
print(a)

a.reverse()
print('a.reverse()')
print(a)

a.sort()
print('a.sort')
print(a)

a.pop()
print('a.pop()')
print(a)

print('deque from collections')
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival

