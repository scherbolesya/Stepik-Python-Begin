# Code-6 review
# A natural number is received for processing. You need to write a program that displays the product of the digits of the entered number.
# The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 3 of them). Each error is known to affect only one line and can be corrected
# without changing other lines.
Ревью кода-6
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа. 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 3). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
