# Arithmetic strings
# Introduced 3 lines in random order. Write a program that finds out whether an arithmetic progression can be constructed from the lengths of these strings.

# Арифметические строки
# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.


a, b, c = len(input()), len(input()), len(input())
if (max(a,b,c)+min(a,b,c))/2 ==(a+b+c-max(a,b,c)-min(a,b,c)): #среднее значение кот должно быть при прогресси и == наше данное(3е число) среднее
    print('YES')
else:
    print('NO')
  

Sample Input 1:
abc
a
abcde
Sample Output 1:
YES
Sample Input 2:
2434
90099
21
Sample Output 2:
NO
Sample Input 3:
aaaaaaaaaa10
1111111Nm
22222r
Sample Output 3:
YES
