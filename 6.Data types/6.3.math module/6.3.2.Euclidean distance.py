# Euclidean distance
# On the plane, the Euclidean distance between two points (x1;y1) and (x2;y2) is defined as ρ=root((x1−x2)2+(y1−y2)**2)
# Write a program that determines the Euclidean distance between two points whose coordinates are given.

# Евклидово расстояние
На плоскости евклидово расстояние между двумя точками (x1;y1) и (x2;y2) определяется так ρ=корень((x1−x2)2+(y1−y2)**2)
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.


import math 
x1 = float(input()) #евклидово расстояние
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(p)


Sample Input 1:
2.0
2.5
44.155
100.50
Sample Output 1:
106.68197610187018
Sample Input 2:
5.5
2.4
4.9
6.3
Sample Output 2:
3.9458839313897713
Sample Input 3:
150.0
100.0
50.0
10.0
Sample Output 3:
134.5362404707371
