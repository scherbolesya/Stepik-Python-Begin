# Build a program that calculates the sum of the digits of the entered natural number.
Cоберите программу, вычисляющую сумму цифр введенного натурального числа.

n = int(input())
total = 0
while n != 0:
last_digit = n % 10
total += last_digit
n //= 10
print(total)
