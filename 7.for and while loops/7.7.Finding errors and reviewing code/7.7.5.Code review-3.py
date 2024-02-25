# Code review-3
# A sequence of 7 integers (each on a separate line) is received for processing. You need to write a program
# which counts and displays the sum of all even numbers in a sequence or 0 if there are no even numbers in the sequence.
# The programmer was in a hurry and wrote the program incorrectly.
# Find all the errors in this program (there are exactly 4 of them). It is known that each error affects only one line and may
# be corrected without changing other lines.
# Note. If necessary, you can add the necessary lines of code.
Ревью кода-3
На обработку поступает последовательность из 7 целых чисел (каждое на отдельной строке). Нужно написать программу, 
которая подсчитывает и выводит сумму всех чётных чисел последовательности или 0, если чётных чисел в последовательности нет. 
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может 
быть исправлена без изменения других строк.
Примечание. При необходимости вы можете добавить необходимые строки кода.

s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)
