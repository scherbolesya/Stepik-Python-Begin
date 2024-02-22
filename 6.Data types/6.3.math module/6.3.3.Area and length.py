# Area and length
# Write a program to determine the area of a circle and the circumference of a circle at a given radius R.
# Note. Use the math.pi constant.

# Площадь и длина
# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
# Примечание. Используйте константу math.pi. 


from math import *
R = float(input())
S = pi*R**2
C =2*pi*R
print(S)
print(C)


Sample Input 1:
554.6
Sample Output 1:
966294.7126386268
3484.654571361799
Sample Input 2:
3.14
Sample Output 2:
30.974846927333925
19.729201864543903
Sample Input 3:
5.5
Sample Output 3:
95.03317777109125
34.55751918948772
