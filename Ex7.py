#!/usr/bin/env python2

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print('a = set(\'abracadabra\')')
print('b = set(\'alacazam\')')
print('a = ',a)                                  # unique letters in a
print('b = ',b)
print('print(a - b)')
print(a - b)                              # letters in a but not in b
print('print(b - a)')
print(b - a)                              # letters in a but not in b
print('print(a | b)')
print(a | b)                              # letters in either a or b
print('print(a & b)')
print(a & b)                              # letters in both a and b
print('print(a ^ b)')
print(a ^ b)                              # letters in a or b but not both

aia = {x for x in 'abracadabra' if x not in 'abc'}
print("aia = {x for x in 'abracadabra' if x not in 'abc'}")
print('aia =',aia)
import string
print(string.digits)


