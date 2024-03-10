Список делителей
На вход программе подается натуральное число n. Напишите программу, которая создает список, состоящий из делителей введенного числа.
# List of divisors
# The program input is a natural number n. Write a program that creates a list of divisors of the entered number.

a = []
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        a.append(i)
print(a)


Sample Input 1:
17
Sample Output 1:
[1, 17]
Sample Input 2:
25
Sample Output 2:
[1, 5, 25]
Sample Input 3:
36
Sample Output 3:
[1, 2, 3, 4, 6, 9, 12, 18, 36]
