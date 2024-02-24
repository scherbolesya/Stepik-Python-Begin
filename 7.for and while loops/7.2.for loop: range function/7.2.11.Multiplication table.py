# Multiplication table
# Таблица умножения
Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n (от 1 до 10 включительно).
Примечание. В качестве знака умножения используйте английскую букву x.
# Given a natural number n. Write a program that prints the multiplication table for n (from 1 to 10 inclusive).
# Note. Use the English letter x as the multiplication sign.

  
n = int(input()) #Таблица умножения
for i in range(0,10):
    print(n, 'x', i+1, '=', n*(i+1))
  
  
Sample Input 1:
5
Sample Output 1:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Sample Input 2:
9
Sample Output 2:
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
Sample Input 3:
4
Sample Output 3:
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
