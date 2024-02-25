# Numerical triangle 3
# Given a natural number n. Write a program that prints a numerical triangle with height equal to n, following the example:
# Note. Use a nested for loop.
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

1
121
12321
1234321
123454321
...

Примечание. Используйте вложенный цикл for.


n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
                
        print(j,end='')
    for k in range(i-1,0,-1):
            print( k, end='')
    print()
                                      
                                     
Sample Input 1:
2
Sample Output 1:
1
121
Sample Input 2:
3
Sample Output 2:
1
121
12321
Sample Input 3:
5
Sample Output 3:
1
121
12321
1234321
123454321
