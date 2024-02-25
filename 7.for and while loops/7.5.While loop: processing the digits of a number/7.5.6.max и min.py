# max и min
# Given a natural number n,(n≥10). Write a program that determines its maximum and minimum digits.
Дано натуральное число n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.


num = int(input())
x = num%10 
n = num%10
while num != 0:
    c = num%10
    if x > c and c < n:
        n = c
    elif x < c and c > n:
        if n > x:
            n = x
        x = c
    elif x > c and c < n:
        n = c
    elif x < c and c < n:
        n = c
    num = num//10
print('Максимальная цифра равна', x)
print('Минимальная цифра равна', n)


Sample Input 1:
26670
Sample Output 1:
Максимальная цифра равна 7
Минимальная цифра равна 0
Sample Input 2:
8945
Sample Output 2:
Максимальная цифра равна 9
Минимальная цифра равна 4
Sample Input 3:
7645897791
Sample Output 3:
Максимальная цифра равна 9
Минимальная цифра равна 1
