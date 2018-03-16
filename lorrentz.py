from vpython import *
from operator import mod
import sys

jl=1.
h=0.01
a=10
b=28
c=8./4.
x0=0.1
y0=0
z0=0
n=10000.
r=1.
try:
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
except IndexError:
    pass

print("Initial value set to:\n a: {}\n b: {}\n c: {}".format(a,b,c))

while jl < n:
    rate(50)
    rd=mod(n,jl)/1000
    sphere(pos=vector(x0,y0,z0),radius=r, color=vector(rd,1,rd))
    x1=x0+h*a*(y0-x0)
    y1=y0+h*(x0*(b-z0)-y0)
    z1=z0+h*(x0*y0-c*z0)
    jl=jl+1
    x0=x1
    y0=y1
    z0=z1

