# Intersection of segments 🌶️🌶️
# There are two segments on the number line: [a1;b1] and [a2;b2]. Write a program that finds their intersection.
# The intersection of two segments can be:
# line segment;
# dot;
# empty set.

# Пересечение отрезков 🌶️🌶️
# На числовой прямой даны два отрезка: [a1;b1] и [a2;b2]. Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть:
# отрезок;
# точка;
# пустое множество.

a1 = int(input())    # пересечение отрезков
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == b2:
    print(a1)
elif a2 == b1:
    print(a2)
elif a1<=a2<b1 and a1<b2<=b1:
    print(a2, b2)
elif a2<a1<b2 and a2<b1<=b2:
    print(a1, b1)
elif a1<=a2<b1 and a1<b1<b2:
    print(a2, b1)
elif a2<a1<b2 and a1<b2<b1:
    print(a1, b2)
else:
    print('пустое множество')
# Sample Input 1:
# 1
# 3
# 2
# 4
# Sample Output 1:
# 2 3
# Sample Input 2:
# 1
# 2
# 3
# 4
# Sample Output 2:
# пустое множество
# Sample Input 3:
# 5
# 6
# 6
# 8
# Sample Output 3:
# 6
