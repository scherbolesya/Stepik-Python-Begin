# Largest and smallest
# Write a program that finds the smallest and largest of five numbers.

# Наибольшее и наименьшее
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input()) 
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))


Sample Input 1:
1
2
3
4
5
Sample Output 1:
Наименьшее число = 1
Наибольшее число = 5
Sample Input 2:
454
453
32
8
6769
Sample Output 2:
Наименьшее число = 8
Наибольшее число = 6769
Sample Input 3:
-3
-11
-499
-888
0
Sample Output 3:
Наименьшее число = -888
Наибольшее число = 0
