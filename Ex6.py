#!/usr/bin/env python2

t = 12345, 54321, 'hello!'
t[0]

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
#ERROR: t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
print('Tuple(krotki) z 0 i jednym elementem:')
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)

print(singleton)
x, y, z = t
print(x)
print(y)
print(z)

