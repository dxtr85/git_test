#!/usr/bin/env python2

tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print("tel['guido'] = 4127")
print(tel)

tel['jack']

del tel['sape']
print("del tel['sape']")
tel['irv'] = 4127
print("tel['irv'] = 4127")
print(tel)
tel['irv'] = 4444
print("tel['irv'] = 4444")
print(tel)


print(list(tel.keys()))

sorted(tel.keys())

'guido' in tel

'jack' not in tel

a = dict([('wito', 4139), ('marto', 4127), ('jakubo', 4098)])
print(a)
b = {x: x**2 for x in (2, 4, 6)}
print(b)
c= dict(xxxx=4139, yyyyy=4127, zzzz=4098)

print(c)

#klucz i wartosc mozna uzyskac przez items():
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#index i zawartosc listy mozna uzyskac przez enumerate(lista):
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#funkcja zip() pozwala na iteracje w wiecej niz jednej lisciejednoczesnie:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#odwrotna kolejnosc mozna zrobic tak:
for i in reversed(range(1, 10, 2)):
    print(i)

#sortowanie zwraca nowa liste
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#Przy zmianie zawartoscli listy po ktorej iterujemy
#lepiej jest stworzyc jej kopie:
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

words

