# Build a program that calculates the sum of numbers from 1 to the entered natural number n.
Cоберите программу, вычисляющую сумму чисел от 1 до введенного натурального числа n.

n = int(input())
total = 0
for i in range(1, n + 1):
total += i
print(total)
