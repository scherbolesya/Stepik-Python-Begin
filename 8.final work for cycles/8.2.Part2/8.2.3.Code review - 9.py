# Code review - 9
# A sequence of 4 integers is received for processing. It is known that the entered numbers do not exceed 10**8 in absolute value.
# We need to write a program that displays the number of odd numbers in the original sequence and the maximum odd number.
# If there are no odd numbers, you need to display “NO”. The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there may be one or more). It is known that each error affects only one line and can be corrected without changing other lines.
# Note. Please note that you need to find errors in an existing program, and not write your own, possibly using a different solution algorithm.
Ревью кода - 9
На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**8. 
Нужно написать программу, которая выводит на экран количество нечетных чисел в исходной последовательности и максимальное нечетное число. 
Если нечетных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно, использующую другой алгоритм решения.

n = 4
count = 0
maximum = -10**6-1
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
           
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
