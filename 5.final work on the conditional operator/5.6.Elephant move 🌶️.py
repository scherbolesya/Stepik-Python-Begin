# Elephant move 🌶️
# Given two different squares of a chessboard. Write a program that determines whether a bishop can get from the first square to the second in one move. 
# The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. 
# The program should output “YES” if the bishop’s move from the first cell can get to the second, or “NO” otherwise.
# Note. The chess bishop moves along diagonals.

# Ход слона 🌶️
# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.
# Примечание. Шахматный слон ходит по диагоналям.


a = int(input())
b = int(input())
c = int(input())
d= int(input())
if a-b==c-d or a+b==c+d:
    print('YES')
else:
    print('NO')
  

Sample Input 1:
4
4
5
5
Sample Output 1:
YES
Sample Input 2:
4
4
5
4
Sample Output 2:
NO
Sample Input 3:
4
4
5
3
Sample Output 3:
YES
