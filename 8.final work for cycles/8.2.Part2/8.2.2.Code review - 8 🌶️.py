# Code review - 8 🌶️
# A sequence of 8 integers is received for processing. It is known that the entered numbers do not exceed 10**12 in absolute value.
# We need to write a program that displays the number of numbers divisible by 4 in the original sequence and the maximum number divisible by 4. If divisible by even
# There are no 4 numbers, you need to display “NO” on the screen. The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there may be one or more). It is known that each error affects only one line and can be corrected without changing other lines.
# Note. Please note that you need to find errors in an existing program, and not write your own, possibly using a different solution algorithm.
Ревью кода - 8 🌶️
На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**12. 
Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 
4 чисел нет, на экран требуется вывести «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.

n = 8
count = 0
maximum = -10**6-1
for i in range(1, n+1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
