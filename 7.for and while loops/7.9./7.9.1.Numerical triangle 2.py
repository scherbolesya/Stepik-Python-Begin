# Numerical triangle 2
# Given a natural number n. Write a program that prints a numerical triangle with height equal to n, following the example:
# Note. Use a nested for loop.
Численный треугольник 2
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...

Примечание. Используйте вложенный цикл for.


n = int(input()) 
total = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        total +=1
        print(total, end=' ')
    print()
                                      
                                      
Sample Input:
3
Sample Output:
1
2 3
4 5 6
