#!/usr/bin/python 

def func(a,n):
        if a>n:
                print a
        else:
                print n

func(3,4)

def sqr(v):
        return v*v

print sqr(8)
x = [1,2,3,3,4]
print x[:3]
print "value=",len(x)
print type(2+1j)
print type(-1+2j)
print type('this is a string')
print type([1,2,2])
print type((2,3,4))
print range(0,20,3)
print range(20,0,-3)
print type(True)
print (2 **3)
if(3 <> 3):
        print 'ok'
else:
        print 'False'
n=0
while (n<10):
        print n
        n=n+1
