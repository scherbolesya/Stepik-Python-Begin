# Review of code-5 🌶️
# A natural number is received for processing. You need to write a program that displays its first (most significant) digit.
# The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 2 of them). Each error is known to affect only one line and can be corrected
# without changing other lines.
Ревью кода-5 🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру. 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 2). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.

n = int(input())
while n > 0:
    s = n % 10
    n = n //10
print(s)
