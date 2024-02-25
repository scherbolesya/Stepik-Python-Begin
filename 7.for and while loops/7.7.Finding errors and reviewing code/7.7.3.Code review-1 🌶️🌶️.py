# Code review-1 🌶️🌶️
# A sequence of 10 integers (each on a separate line) is received for processing.
# You need to write a program that displays the number of non-negative numbers in a sequence and their product.
# If there are no non-negative numbers, you need to display “NO”. The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 4 of them). Each error is known to affect only one line and can be corrected
# without changing other lines.
# Note. If necessary, you can add the necessary lines of code.
Ревью кода-1 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). 
Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение. 
Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
Примечание. При необходимости вы можете добавить необходимые строки кода.

count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
