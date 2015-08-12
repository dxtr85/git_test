#!/usr/bin/env python2

def defaultValue(a,L=[]): #Wartosc domyslna jest przypisywana tylko raz do funkcji!
    L.append(a)
    return L

def defaultValue2(a,L=None):
    if L==None:
        L=[]
    L.append(a)
    return L

print(defaultValue(1))
print(defaultValue(2))
print(defaultValue(3))

print(defaultValue2(1))
print(defaultValue2(2))
print(defaultValue2(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
"""
#Invalid calls:
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""
