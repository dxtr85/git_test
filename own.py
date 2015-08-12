#!/usr/bin/env python2

import os
import Ex1

python_processes = os.popen("ps -aux| grep python").read()
print(python_processes.__class__)
for i,proc in enumerate(python_processes.split("\n")):
    if proc:    #Jeżeli jest pusta linia to jej nie drukujemy
        print(i,"  ", proc)
dict = {'kuba':6,'witek':5,'marta':4}
for name,value in dict.items():
    print("Nazwa:", name,"wartosc:",value)

Ex1.fib(10000000)
res = Ex1.fib2(334)
print(res)

class WlasnyException(Exception):
    def __init__(self,wartosc):
        self.wart = wartosc
    def why(self):
        print("Niedozwolona wartosc:",self.wart)

class Klasa:
    def __init__(self,name,init=0):
        print("Inicjalizacja")
        self.wart = init
        self.name = name
        self.trick = []

    def zmien(self,nowa):
        self.wart = nowa
    def zwroc(self):
        return self.wart
    def add_trick(self,name):
        self.trick.append(name)
    def print_tricks(self):
        print("Triki",self.name,end=': ')
        for i in self.trick:
            print(i,end=" ")
        print()


k = Klasa("K")
l = Klasa("L")
k.add_trick("lezec")
l.add_trick("siad")
k.print_tricks()
l.print_tricks()

def nowa(self):
    print("Nowa funkcja")
print(k.wart.__class__)
k.wart = nowa
#Klasa.n = nowa

#del Klasa.n
k.n = nowa

#Teraz to nie jest metoda klasy tylko dodana przez nas funkcja, wiec self nie jest do niej domyslnie przekazywane
k.n(k)

print(k.zwroc())
k.zmien(13)
print(k.zwroc())
print("Test")

def funkcja():
    wart = 1
    def test():
        nonlocal wart
        print(wart)
        wart = 2
    test()
    print(wart)
funkcja()

try:
    i = int(input("Podaj liczbe:"))
    if i== 3:
        a = WlasnyException(i)
        raise a
except WlasnyException as e:
    print("dupa")
    e.why()
except ValueError:
    print("\nERROR: Miałeś podać liczbę!\n")
    exit()
else:
    print("i:",i)

print("Poza trajkaczem")
int(input("Daj jako liszpe:"))

