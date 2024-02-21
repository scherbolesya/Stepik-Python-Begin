# Manhattan distance
# Walking around Manhattan, you can't get from point A to point B by taking a shortcut. Unless you know how to walk through walls, 
# you will definitely have to walk along its parallel-perpendicular streets.
# (p1;p2) and (q1;q2) is defined as ∣p1−q1∣+∣p2−q2∣.
# Write a program that determines the Manhattan distance between two points whose coordinates are given.

# Манхэттенское расстояние
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены, 
# вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# На плоскости манхэттенское расстояние между двумя точками 
# (p1;p2) и (q1;q2) определяется так ∣p1−q1∣+∣p2−q2∣.
# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p1 = int(input()) # манхэттенское расстояние
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1-q1)+abs(p2-q2))

Sample Input:
10
15
21
13
Sample Output:
13
