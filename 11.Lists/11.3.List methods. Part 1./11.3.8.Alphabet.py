# Alphabet
# Write a program that produces the following list:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Note 1: The last element of the list must consist of 26 z characters.
# Note 2. English alphabet (for copying) 😇:
# abcdefghijklmnopqrstuvwxyz
Алфавит
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Примечание 1. Последний элемент списка должен состоять из 26 символов z.
Примечание 2. Английский алфавит (для копирования) 😇:
abcdefghijklmnopqrstuvwxyz


abc = ' abcdefghijklmnopqrstuvwxyz'
a = list()
for i in range(1,27):
        s = abc[i]*i
        a.append(s)
print(a)
