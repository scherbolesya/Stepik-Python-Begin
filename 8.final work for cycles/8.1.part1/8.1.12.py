# Build a program that calculates the number of digits of an entered natural number.
# Note. First increase the counter.
Соберите программу, вычисляющую количество цифр введенного натурального числа.
Примечание. Сначала увеличьте счетчик.

n = int(input())
counter = 0
while n > 0:
counter += 1
n //= 10
print(counter)
