# Triangle inequality
# Неравенство треугольника

# Write a program that takes three positive numbers and determines whether a non-degenerate triangle with those sides exists.
# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
# a+b>c
# a+c>b
# b+c>a

a = int(input())
b = int(input())
c = int(input())
if a < b+c and b < a+c and c < a+b:
    print('YES')
else:
    print('NO')
  
# Sample Input 1:
# 5
# 2
# 3
# Sample Output 1:
# NO
# Sample Input 2:
# 3
# 4
# 6
# Sample Output 2:
# YES
# Sample Input 3:
# 8
# 2
# 4
# Sample Output 3:
# NO
