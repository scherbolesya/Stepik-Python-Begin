# Reciprocal number
# Write a program that reads one number from the keyboard and prints its inverse. If the number entered from the keyboard is zero, then print “There is no reciprocal number” (without quotes).

# Обратное число
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

a = float(input())
if a == 0:
    print ('Обратного числа не существует')
elif a != 0:
    print(1/a)
  

Sample Input 1:
2.5
Sample Output 1:
0.4
Sample Input 2:
-55.6
Sample Output 2:
-0.017985611510791366
Sample Input 3:
0
Sample Output 3:
Обратного числа не существует
