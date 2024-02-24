# Sum of divisors
Сумма делителей
На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.
# The program input is a natural number n. Write a program that calculates the sum of all its divisors.
# Note. The function of calculating the sum of all divisors of a number is very important in number theory.


total = 0
n = int(input())
for i in range(1,n+1):
    if n%i ==0:
        total +=i
print(total)


Sample Input 1:
10
Sample Output 1:
18
Sample Input 2:
50
Sample Output 2:
93
Sample Input 3:
3
Sample Output 3:
4
