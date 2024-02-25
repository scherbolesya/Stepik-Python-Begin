# Code review 2 🌶️🌶️
# A sequence of 10 integers (each on a separate line) is received for processing.
# It is known that the entered numbers do not exceed 10**6 in absolute value. You need to write a program
# which displays the sum of all negative numbers in the sequence and the maximum negative number in the sequence.
# If there are no negative numbers, you need to display “NO”. The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 5 of them). Each error is known to affect only one line and can be corrected
# without changing other lines.
# Note. If necessary, you can add the necessary lines of code.
Ревью кода-2 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). 
Известно, что вводимые числа по абсолютной величине не превышают 10**6. Нужно написать программу, 
которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности. 
Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
Примечание. При необходимости вы можете добавить необходимые строки кода.

mx = -10000
s = 0
for i in range(1,11):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s == 0:
    print('NO')
else:
    print(s)
    print(mx)
