# Code review - 7 🌶️
# A natural number is received for processing. You need to write a program that displays the sum of the even digits of this number or 0 if there are no even digits in the entry.
# The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there may be one or more). It is known that each error affects only one line and can be corrected without changing other lines.
# Note. Please note that you need to find errors in an existing program, and not write your own, possibly using a different solution algorithm.
Ревью кода - 7 🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму четных цифр этого числа или 0, если четных цифр в записи нет. 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s = s + n % 10
    n //= 10
print(s)
