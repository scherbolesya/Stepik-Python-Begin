# star frame
# The program input is a natural number n. Write a program that prints a star frame with dimensions n×19.
# Input format
# The input to the program is a natural number n∈[3;19] - the height of the star frame.
# Output format
# The program should output a star frame with dimensions n×19.
# Clue. To print a star line, use multiplying the line by the number.
Звездная рамка
На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19.
Формат входных данных
На вход программе подаётся натуральное число n∈[3;19] — высота звездной рамки.
Формат выходных данных
Программа должна вывести звездную рамку размерами n×19.
Подсказка. Для печати звездной линии используйте умножение строки на число.


n = int(input())
print(19*'*')
for i in range(n-2):
    print('*',' '*17,'*',sep='')
print(19*'*')

  

Sample Input 1:
3
Sample Output 1:
*******************
*                 *
*******************
Sample Input 2:
4
Sample Output 2:
*******************
*                 *
*                 *
*******************
Sample Input 3:
5
Sample Output 3:
*******************
*                 *
*                 *
*                 *
*******************
