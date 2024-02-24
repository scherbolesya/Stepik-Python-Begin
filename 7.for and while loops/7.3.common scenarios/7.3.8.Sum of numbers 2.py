# Sum of numbers 2
# Сумма чисел 2
На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), 
квадрат которых оканчивается на 2,5 или 8.
# The program input is a natural number n. Write a program that calculates the sum of those numbers from 1 to n (inclusive) whose square ends in 2.5 or 8.

  
total = 0  
n = int(input())
for i in range(1,n+1):
    if (i**2)%10==2 or (i**2)%10==5 or (i**2)%10==8:
        total +=i
print(total)


Sample Input 1:
10
Sample Output 1:
5
Sample Input 2:
100
Sample Output 2:
500
Sample Input 3:
1992
Sample Output 3:
198005
