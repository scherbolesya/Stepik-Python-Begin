# Queen move
# Given two different squares of a chessboard. Write a program that determines whether the queen can get from the first square to the second in one move. 
# The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. 
# The program should output “YES” if it is possible to get from the first cell by moving the queen to the second, or “NO” otherwise.
# Note. The chess queen moves diagonally, horizontally or vertically.

# Ход ферзя
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.
# Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.

x1=int(input()) #ход ферзя
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)==abs(y1-y2) or x1==x2 or y1==y2:
    print('YES')
else:
    print('NO')
  

Sample Input:
1
1
2
2
Sample Output:
YES
