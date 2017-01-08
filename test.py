#!/usr/bin/python

def funkcja2(a, b, c, **kwargs):
    print ('funkcja2: a: %s b: %s c: %s' %(a,b,c))
    print ('funkcja2: kwargs %s' %str(kwargs))
    funkcja3(**kwargs)

def funkcja3(d, **kwargs):
    print('funkcja3: d %s' %d)

def funkcja1(params):
    print "funkcja1: Paramsy: %s" %str(params)
    funkcja2(**params)
    
if __name__ == '__main__':
    print 'Main'
    d = {'a':'aA','b':'bB','c':'cC', 'd':'dD'}
    funkcja1(d)

