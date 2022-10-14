#Assignment operators
from ast import operator


Q = 5
W = 8

Q *=W
print ('Q=',Q)

E = 10
R = 4
E /=R
print('E=',E)

R %= 2
print('R=',R)



T = 9
T //=2
print ("T=",T)

Y = 15
Y **=5
print('Y=',Y)

#Comparison Operators

X=10
if X >= 8:
  print("Greater or Equal")
else:
  print("Not Greater or Equal" )

Y=10
if Y<= 18:
  print("less or Equal")
else:
  print("Not less or Equal" )

#Logical operator

A=11
if A>10 and A<18:
  print("A=",A)
else:
  print("Not in range")

B=18
if B>10 or B>18:
  print("B=",B)
else:
  print("Not in range")