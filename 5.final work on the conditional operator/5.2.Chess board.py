# Chess board
# Two squares of a chessboard are given. Write a program that determines whether the given cells have the same color or not. 
# If they are painted the same color, then print the word “YES”, and if they are painted in different colors, then print “NO”.
# Шахматная доска
# Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. 
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».

a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if (a+b+a1+b1)%2==0:
    print('YES')
else:
    print('NO')

Sample Input 1:
1
1
2
6
Sample Output 1:
YES
Sample Input 2:
2
2
2
5
Sample Output 2:
NO
