from math import *
a=eval(input("Input a value for a:"))
b=eval(input("Input a value for b:"))
c=eval(input("Input a value for c:"))
D=b**2-4*a*c
if D>0:
    x1=(-b+sqrt(b**2-4*a*c))/2*a
    x2=(-b-sqrt(b**2-4*a*c))/2*a
    print(f"The first solution is:",x1,", the second solution is:",x2,"")
elif D==0:
    x1=(-b+sqrt(b**2-4*a*c))/2*a
    print(f"The solution is:",x1,"")
elif D<0:
    print(f"There are no solutions")

