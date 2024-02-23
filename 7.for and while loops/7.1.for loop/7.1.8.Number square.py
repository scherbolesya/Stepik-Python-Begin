# Number square
# Квадрат числа
# На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
# The program input is a natural number n. Write a program that, for each number from 0 to n (inclusive), prints the phrase: “The square of [number] is equal to [number]” (without quotes).


n = int(input())
for i in range(n+1):
    print('Квадрат числа', i, 'равен', i**2)
  

Sample Input 1:
9
Sample Output 1:
Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Квадрат числа 2 равен 4
Квадрат числа 3 равен 9
Квадрат числа 4 равен 16
Квадрат числа 5 равен 25
Квадрат числа 6 равен 36
Квадрат числа 7 равен 49
Квадрат числа 8 равен 64
Квадрат числа 9 равен 81
Sample Input 2:
1
Sample Output 2:
Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Sample Input 3:
2
Sample Output 3:
Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Квадрат числа 2 равен 4
