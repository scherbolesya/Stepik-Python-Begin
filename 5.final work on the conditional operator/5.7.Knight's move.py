# Knight's move
# Given two different squares of a chessboard. Write a program that determines whether a knight can get from the first square to the second in one move. 
# The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. 
# The program should output “YES” if the knight’s move from the first cell can get to the second, or “NO” otherwise.
# Note. The chess knight moves in the letter "G". 

# Ход коня
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.
# Примечание. Шахматный конь ходит буквой «Г».

a = int(input())   #ход коня
b = int(input())
a1 = int(input())
b1 = int(input())
x = abs(a-a1)
y = abs(b-b1)
if (x==1 and y ==2) or (x==2 and y==1):
    print("YES")
else:
    print('NO')
  

Sample Input 1:
1
1
8
8
Sample Output 1:
NO
Sample Input 2:
2
4
3
2
Sample Output 2:
YES
