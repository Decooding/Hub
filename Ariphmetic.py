#Введение в Пайтон стр 13#
from math import*

x1 = int(input("x1="))
x2 = int(input("x2="))
x3 = int(input("x3="))
y1 = int(input("y1="))
y2 = int(input("y2="))
y3 = int(input("y3="))

a = sqrt((x1-x2)**2+(y1-y2)**2)
b = sqrt((x1-x3)**2+(y1-y3)**2)
c = sqrt((x2-x3)**2+(y2-y3)**2)

p=(a+b+c)/2
h=2*sqrt(p*(p-a)*(p-b)*(p-c))/a
m=sqrt(2*b**2+2*c**2-a**2)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))

print('H=',h, 'M=',m, 'S=',s)
