# Review of code-4 🌶️🌶️
# A natural number is received for processing. We need to write a program that displays the maximum digit of a number that is a multiple of 3.
# If the number does not contain digits that are multiples of 3, you need to display “NO” on the screen. The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 5 of them). Each error is known to affect only one line and can be corrected
# without changing other lines.
# Note 1. The number 0 is divisible by any natural number.
# Note 2: You can add the required lines of code if necessary.
Ревью кода-4 🌶️🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3. 
Если в числе нет цифр, кратных 3, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
Примечание 1. Число 0 делится на любое натуральное число.
Примечание 2. При необходимости вы можете добавить нужные строки кода.

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
