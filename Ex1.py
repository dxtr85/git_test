#!/usr/bin/env python2
import sys

def fib(n): #Fibonacci function
    """Print a Fibonacci series up to n."""
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()

def fib2(n): #Returns a list of Fibonacci series up to n
    a,b=0,1
    result = []
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

def askOk(prompt,retries=4,complaint="C'mon, only 'yes' or 'no' allowed."):
  while True:
    ok=input(prompt)
    if ok in ('y', 'ye', 'yes'):
        return True
    if ok in ('n', 'no'):
        return False
    retries = retries - 1
    print(complaint)
    if retries <= 0:
        raise OSError('User ma cię w nosie.')

def main():
    fibResult = fib2(int(sys.argv[1]))

    print(fib(0))
    print(fibResult)
    if askOk("Do you want to quit?[yes/no]: "):
        print("Bye")
    else:
        print("Bye anyway :P")

if __name__ == "__main__":
    main()
