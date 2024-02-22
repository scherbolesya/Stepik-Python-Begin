# Regular polygon
# # A regular polygon is a convex polygon in which all sides and all angles between adjacent sides are equal. The area of a regular polygon with side length a and number of sides n is calculated by the formula:
# Given two numbers: a natural number n and a real number a. Write a program that finds the area of a given regular polygon.

# Правильный многоугольник
# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле: 
# Даны два числа: натуральное число n и вещественное число a. Напишите программу, которая находит площадь указанного правильного многоугольника.


from math import *  # правильный многоугольник
n = float(input())
a = float(input())
S = (n*a**2)/(4*tan(pi/n))
print(S)


Sample Input:
3
2.0
Sample Output:
1.7320508075688779
