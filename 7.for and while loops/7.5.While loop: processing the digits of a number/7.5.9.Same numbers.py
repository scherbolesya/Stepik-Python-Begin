#  Same numbers
# A natural number is given. Write a program that determines whether a given number consists of identical digits.
Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.


num = input() 
x = max(num)
n = min(num)
if x == n:
    print('YES')
else:
    print('NO')


Sample Input 1:
11111
Sample Output 1:
YES
Sample Input 2:
11112111
Sample Output 2:
NO
