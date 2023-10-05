from login import login
import  oprations as op
import math as m
#print(dir(m))

if(login()):
    str=input("enter a string")
    op.strrev(str)

    a=int(input("enter a  value"))
    b=int(input("enter b  value"))
    print("addition",op.add(a,b))
