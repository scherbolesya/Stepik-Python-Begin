# Quadratic Equation 🌶️🌶️
# # Given three real numbers a, b, c. Write a program that finds the real roots of the quadratic equation: ax**2+bx+c=0.
If an equation has two roots, then they should be derived in ascending order.
  
# Квадратное уравнение 🌶️🌶️
# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения: ax**2+bx+c=0.
Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

  
from math import *
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
if D<0:
    print('Нет корней')
elif D==0 and a !=0:
    x =-b/(2*a)
    print(x)
elif D>0 and a !=0:
    x1 =(-b+sqrt(D))/(2*a)
    x =(-b-sqrt(D))/(2*a)
    print(min(x,x1))


Sample Input 1:
1
2
1
Sample Output 1:
-1.0
Sample Input 2:
1
-7.5
3
Sample Output 2:
0.4239663260874824
7.076033673912518
