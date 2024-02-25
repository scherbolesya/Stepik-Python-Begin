# Numerical triangle 1
# Given a natural number n. Write a program that prints a numerical triangle as per the example:
1
22
333
4444
55555
...
# Note. Use a nested for loop.
Численный треугольник 1
Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:

1
22
333
4444
55555
...

Примечание. Используйте вложенный цикл for.


                                      
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end='')
    print()


                                      
Sample Input:
5
Sample Output:
1
22
333
4444
55555
