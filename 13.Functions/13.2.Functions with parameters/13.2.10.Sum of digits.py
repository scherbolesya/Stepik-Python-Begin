# Sum of digits
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
# Write a function print_digit_sum() that takes a single integer num and prints the sum of its digits.

# объявление функции
def print_digit_sum(num):
    a = 0
    while num != 0:
        a = a + (num%10)
        num = num//10
    print(a)
# считываем данные
n = int(input())
# вызываем функцию
print_digit_sum(n)

  
Sample Input 1:
12345
Sample Output 1:
15
Sample Input 2:
12
Sample Output 2:
3
Sample Input 3:
7
Sample Output 3:
7
