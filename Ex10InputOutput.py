#!/usr/bin/env python2

# Obiekty mozna wyswietlic przy uzyciu str() i repr()
s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

##
# Dwa sposoby na zapisywanie ladnie formatowanych stringow:

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#Wypelnianie zerami:
'12'.zfill(5)

'-3.14'.zfill(7)

'3.14159265359'.zfill(5)

#Uzycie string.format():
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

#Wykorzystanie argumentow nazwanych:
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))

### '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
import math
print('The value of PI is approximately {}.'.format(math.pi))

print('The value of PI is approximately {!r}.'.format(math.pi))

print('The value of PI is approximately {0:.3f}.'.format(math.pi))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

#Uzycie slownika do formatowania stringa:
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
#i mozna tak:
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# Odczyt i zapis do pliku:
f = open('workfile', 'w')

# 1szy arg - nazwa pliku, drugi, opcjonalny arg - tryb (moze byc r,w,r+ i dodatkowo b(inary)
# domyslnie 2gi jest r(ead)

fileObject.read() # czyta caly plik
fileObject.readline() # czyta jedna linie
for line in fileobject:
	#iteruje po liniach w pliku
fileObject.write(obiekt) #zapisuje obiekt w pliku, zwraca ilosc zapisanych bajtow/znakow

## Zapis binarny:
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)     # Go to the 6th byte in the file

f.read(1)

# 2gi argument 0 (default) od poczatku pliku, 1 - od akt.pozycji, 2- od konca pliku
# seek() najbezpieczniej jest stosowac z plikami binarnymi

f.seek(-3, 2) # Go to the 3rd byte before the end

f.read(1)

f.close() # po tym obiekt f juz nie jest dostepny

# bezpieczniejszy sposob na operowanie na pliku i pewnosc ze potem zostanie zamkniety:
with open('workfile', 'r') as f:
    read_data = f.read()
f.closed #True

# serializowanie danych do pliku przez json modul:
json.dumps([1, 'simple', 'list'])

json.dump(x, f)

x = json.load(f)


