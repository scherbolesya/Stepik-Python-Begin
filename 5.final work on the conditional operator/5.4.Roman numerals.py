# Roman numerals
# Write a program that reads an integer and prints its corresponding Roman numeral. If the number is out of range 1−10, then the program should display the text “error”.
# The table shows Roman numerals for numbers from 1 to 10.

# Римские цифры
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1−10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.

Число	Римская цифра
1	I
2	II
3	III
4	IV
5	V
6	VI
7	VII
8	VIII
9	IX
10	X


a = int(input()) #меняет число на римское
if a == 1:
    print("I")
elif a == 2:
    print('II')
elif a == 3:
    print('III')
elif a == 4:
    print('IV')
elif a == 5:
    print('V')
elif a == 6:
    print('VI')
elif a == 7:
    print('VII')
elif a == 8:
    print('VIII')
elif a == 9:
    print('IX')
elif a == 10:
    print('X')
else:
    print('ошибка')


Sample Input 1:
7
Sample Output 1:
VII
Sample Input 2:
12
Sample Output 2:
ошибка
